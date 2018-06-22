
$ ./ar2afd "(aa)*(b + aba)(aa)*" > afd.json
$ ./json2dot.sh afd.json > afd.dot
$ dot -Tpdf -o afd.pdf afd.dot
