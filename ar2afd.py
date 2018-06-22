#!/usr/bin/env python3
import sys

# Authors: Takahashi -- Raylander

#(0+1)*0

tab2={}
m=[]
tab3 = {}
fs=[]
tab={}
voc=[]

def jason(qf):
	txt="{ \"af\":["

	num=0
	txt2 = ""
	txt+="["
	aux = []
	for a in fs :
		txt3 = ""
		if len (a) > 1:
			txt3+= "\""
			for b in a:
				txt3+=str(b)
				txt3+=", "
				aux.append("\""+str(b)+"\"")
			txt3+="\", " 
		
			#print(txt3[:len(txt3)-5]+"\"")
			txt2+=txt3[:len(txt3)-5]+"\", "
		else:
			txt2+= "\""+str(a[0])+"\", "
			aux.append("\""+str(a[0])+"\"")



	txt+=txt2[:len(txt2)-2]
	txt+="], "

	txt2 = ""
	txt+="["

	for a in voc :
		txt2+= "\""
		txt2+=str(a)
		txt2+="\", " 
	
	txt+=txt2[:len(txt2)-2]
	txt+="],"

	txt+="[ \n"
	
	txt2 = ""

	while num < len(fs):
		txt3 = ""
		for b in voc: 
			
			if tab3.get((num,b), False):
				
				txt3 += "["
				txt3 += aux[num]
				txt3 += ", "
				txt3 += "\"" 
				txt3 += b
				txt3 += "\", "
				i=0
				while(i < len(fs)):
					
					if(tab3[num, b] == fs[i]):
						txt3 += aux[i]
					i+=1
				txt3 += "], "
		
		txt2 += txt3[:len(txt3)-1]	
		num += 1

	if len(txt2) != 0:
		txt+=txt2[:len(txt2)-2]+"]"
	txt += "\n],"
	txt += "["+aux[0]+"], "
	
	txt+= "["
	num = 0
	txt2 = ""
	for a in fs:
		if qf in tab2[num, '#']:
			txt2+= aux[num]+","
		num+=1
	
	txt += txt2[:len(txt2)-1]+"]" 

	txt += "\n]"+"\n}"

	print(txt)


def transLam(a):
	j = int(a)
	aux = []
	
	if tab.get((j, '#'), False):
		aux = tab[j,'#']
		
		j= 0
		# gera primeiro estado novo 
		while j < len(aux):	
										
			if tab.get((aux[j], '#'), False): 
				a = tab[aux[j], '#']

				for b in a:
					if not( b in aux):
						aux.append(b)	
			j+=1
	return aux

def afnL_to_afn(qi):
	qi = int(qi)
	#fs=[]
	num = 0
	fs.append([qi])
	j = 0

	k = -1 
	while (k < len(voc)):
		if(voc[k] == '#'):
			del voc[k]
		k+=1
	
	while j < len (fs): # enquanto todos não foram encontrados 
		

		aux3 = fs[num]	 
		aux = []

		for a in aux3:

			d = str(a)
			b = transLam(d)
			
			for c in b:
				if	not(c in aux):
					aux.append(c)

		tab2[num,'#'] = aux

		for v in voc:
			
			aux2 = []
			for a in aux:
				if tab.get((a,v), False): # gera transição entre os estados novos 

					for c in tab[a,v]:
						if	not(c in aux2):
							aux2.append(c)

			if len(aux2) != 0:
				if not (aux2 in fs ): 
					fs.append(aux2)
				
				tab3[num,v] = aux2
								
		j+=1
		num+=1
	#print(fs)


## Declarações 


def reg_ex_to_afnL(rE, init_num, qf):

	rE = str(rE) 
	num = int( init_num )
	ou = 0
	call = 1

	qi = num
	aux = num
	aux2 = num
	qf = num
	par = 0
	ret_urn = 1
	aux4=0
	aux3=0

	for l in rE:

		if(ret_urn-1 ==0):
		 # 0 # 1  1 l 2  2 # 3
			if l != '+' and l != '*' and l != '(' and l != ')' and l != ' ' and l !='' and l!= 'EOF':
				
				par = 0
				if  not ( l in voc ):
					voc.append(l)

				if ou == 0:				
#					#print (num)
#					#print (aux)
#					#input()
					# primeiro da ligação
					if not tab.get((num,'#'), False):
						tab[num,'#']=[]
						tab[num,'#'].append(num)
					tab[num,'#'].append(num+1)

					# segundo
					if not tab.get((num+1,'#'), False):
						tab[num+1,'#']=[]
						tab[num+1,'#'].append(num+1)
					
					if not tab.get((num+1,l), False):
						tab[num+1,l]=[]
					tab[num+1,l].append(num+2)

					# terceiro	
					if not tab.get((num+2,'#'), False):
						tab[num+2,'#']=[]
						tab[num+2,'#'].append(num+2)
					tab[num+2,'#'].append(num+3)

					# quarto
					if not tab.get((num+3,'#'), False):
						tab[num+3,'#']=[]
						tab[num+3,'#'].append(num+3)
					
					aux = num
					num += 3
					aux2 = num
					qf = num
				
				elif ou == 2:

					# outra opcao do ou 
					# inicio liga ao primeiro 

					if not tab.get((qi,'#'), False):
						tab[qi,'#']=[]
						tab[qi,'#'].append(num)
					tab[qi,'#'].append(num)

					# o primeiro se gera
					if not tab.get((num,'#'), False):
						tab[num,'#']=[]
						tab[num,'#'].append(num)
					tab[num,'#'].append(num+1) # liga ao proximo

					# o segundo se gera
					if not tab.get((num+1,'#'), False):
						tab[num+1,'#']=[]
						tab[num+1,'#'].append(num+1)
					
					# o segundo gera o terceiro
					if not tab.get((num+1,l), False):
						tab[num+1,l]=[]
						tab[num+1,l].append(num+2)

					# o terceiro se gera 
					if not tab.get((num+2,'#'), False):
						tab[num+2,'#']=[]
						tab[num+2,'#'].append(num+2)
					tab[num+2,'#'].append(num+3) # O terceiro liga ao terceiro 

					if not tab.get((num+3,'#'), False):
						tab[num+3,'#']=[]
						tab[num+3,'#'].append(num+3)
					tab[num+3,'#'].append(qf)# o terceiro liga ao final
					
					aux = num
					num += 3
					aux2 = num
					ou = 1
			
				elif ou == 1:

					# desfaz a ligação ao final
					i = 0 
					while i < len(tab[aux2,'#']):
					#	print(i)
						if (tab[aux2,'#'][i] == qf ):
							tab[aux2,'#'][i] = num
						i+=1

					# o primeiro se gera
					if not tab.get((num,'#'), False):
						tab[num,'#']=[]
						tab[num,'#'].append(num)
					tab[num,'#'].append(num+1) # se liga ao proximo

					# o segundo se gera
					if not tab.get((num+1,'#'), False):
						tab[num+1,'#']=[]
						tab[num+1,'#'].append(num+1)
					
					# o segundo se liga ao terceiro
					if not tab.get((num+1,l), False):
						tab[num+1,l]=[]
					tab[num+1,l].append(num+2)

					# o terceiro se gera
					if not tab.get((num+2,'#'), False):
						tab[num+2,'#']=[]
						tab[num+2,'#'].append(num+2)
					tab[num+2,'#'].append(num+3) # 

						# se liga ao ultimo
					if not tab.get((num+3,'#'), False):
						tab[num+3,'#']=[]
						tab[num+3,'#'].append(num+3)
					tab[num+3,'#'].append(qf) # 

					aux = num
					num += 3
					aux2 = num

			if l == '+':


				if ou == 0:
					# novo inicio
					if not tab.get((num+1,'#'), False):
						tab[num+1,'#']=[]
						tab[num+1,'#'].append(num+1)
					tab[num+1,'#'].append(qi)


					# novo final
					if not tab.get((num+2,'#'), False):
						tab[num+2,'#']=[]
						tab[num+2,'#'].append(num+2)
					tab[aux2,'#'].append(num+2)


					qi = num + 1
					qf = num + 2
					num = num+3
				
				ou = 2
			
			if l == '*':	


				# gera loop
				if par == 0:
					
					if not tab.get((aux2-1,'#'), False):
						tab[aux2-1,'#']=[]
						tab[aux2-1,'#'].append(aux2)
					
					tab[aux2-1,'#'].append(aux2-2)
					
					# o inicio liga ao final
					if not tab.get((aux,'#'), False):
						tab[aux,'#']=[]
						tab[aux,'#'].append(aux2)
					tab[aux,'#'].append(aux2)		
				else:
					if not tab.get((aux4,'#'), False):
						tab[aux4,'#']=[]
						tab[aux4,'#'].append(aux4)
					
					tab[aux4,'#'].append(aux3)
					
					# o inicio liga ao final
					if not tab.get((aux,'#'), False):
						tab[aux,'#']=[]
						tab[aux,'#'].append(aux2)
					tab[aux,'#'].append(aux2)		
					par = 0
					 

			if l == '(':
				if not tab.get((num,'#'), False):
					tab[num,'#']=[]
					tab[num,'#'].append(num)

				aux = num		
				num = num +1
				(ret_urn, num, f, aux3 , aux4) = reg_ex_to_afnL(rE[call:] ,num, qf)
				if not tab.get((num,'#'), False):
					tab[num,'#']=[]
					tab[num,'#'].append(num)
				
				if not ((num+1) in tab[f,'#']):
					tab[f,'#'].append(num+1)
				
				# o primeiro vira um estado 				
				tab[aux,'#'].append(aux3)		
				
				par = 1
				num = num +1 
				aux2 = num

				if ou == 0:
					qf = num	
				elif ou == 2:
					# o inicio se liga ao primeiro
					if not tab.get((qi,'#'), False):
						tab[qi,'#']=[]
						tab[qi,'#'].append(num)
					tab[qi,'#'].append(num)

					# o ultimo se liga ao final
					if not tab.get((num,'#'), False):
						tab[num,'#']=[]
						tab[num,'#'].append(num)
					if not ((qf) in tab[num,'#']):
						tab[num,'#'].append(qf)
					ou = 1
							
			call += 1

			if l == ')':
				return (call, num, qf, qi, qf)

		else:
			call+=1
			ret_urn-=1

	return (call, num, qf, qi, qf) 
			
	
## Main 

reg_ex = str(sys.argv[1:])

reg_ex = reg_ex[2:len(reg_ex)-2]
num =0 

if len(reg_ex) != 0:
	(a,b,c,d,e)=reg_ex_to_afnL(reg_ex,num, 0)

	afnL_to_afn(d)
	jason(c)
	tab = {}
	tab3={}
	voc=[]
fs=[]

#(aa)*(b+a)(aa)*