import sys
import constantes

#Abertura dos arquivos de entrada e saida
inputTxt = open(sys.argv[1],'r')
outputTxt = open(constantes.ARQUIVO_PROCESSADO,'w')

#Carregando o conteudo
with inputTxt as inp:
    conteudo = inp.readlines()

#Ordenando os registros
conteudo.sort()

#Escrevendo registros ordenados no arquivo de saida
with outputTxt as out:
	out.writelines(conteudo)

#Fechando arquivos
inputTxt.close()
outputTxt.close()