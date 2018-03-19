import sys

inputTxt = open("input.txt",'r')
outputTxt = open("arquivo_processado.txt",'w')

with inputTxt as inp:
    conteudo = inp.readlines()

conteudo.sort()
with outputTxt as out:
	out.writelines(conteudo)

inputTxt.close()
outputTxt.close()