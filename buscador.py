import sys
import bisect
import constantes

def encontra_maior(a, x):
 	#Encontra o maior registro menor ou igual a x
    j = bisect.bisect_right(a, x)
    return j

def encontra_menor(a, x):
    #Encontra o menor registro maior ou igual a x
    i = bisect.bisect_left(a, x)
    return i

#Validacao de dados obrigatorios
if (len(sys.argv) < 3):
	print "Forneca data inicial e data final para o algoritmo de busca."
	exit(1)

#Abertura dos arquivos de entrada e saida
inputTxt = open(constantes.ARQUIVO_PROCESSADO,'r')
outputTxt = open(constantes.RESULTADO,'w')

#Iniciando as listas
registro = []
data = []

#Armazena registros ordenados e os formata
for line in inputTxt:
	linha = tuple(line.strip('\n').split(';'))
	registro.append(linha)
	data.append(linha[0])

#Realiza busca por data e retor os indices dos registros
i = encontra_menor(data, sys.argv[1])
j = encontra_maior(data, sys.argv[2])

#Busca apenas por intervalos de datas
if len(sys.argv) == 3:
	outputTxt.write('\n'.join('{} {} {}'.format(x[0],x[1],x[2]) for x in registro[i:j]))

#Filtra por identificador do evento
else:
	condition = list(sys.argv[3:])
	filtro = [x for x in registro[i:j] if x[1] in condition]
	outputTxt.write('\n'.join('{} {} {}'.format(x[0],x[1],x[2]).replace(' ',';') for x in filtro))

#Fecha arquivos de entrada e saida
inputTxt.close()
outputTxt.close()