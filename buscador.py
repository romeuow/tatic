import sys
import bisect

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(a, x)
    if i:
        return i-1
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return i
    raise ValueError

if (len(sys.argv) < 3):
	print "Forneca data inicial e data final para o algoritmo de busca"
	exit(1)

inputTxt = open("arquivo_processado.txt",'r')
outputTxt = open("saida.txt",'w')

registro = []
data = []
tag = []

for line in inputTxt:
	linha = tuple(line.strip('\n').split(';'))
	#print linha
	registro.append(linha)
	data.append(linha[0])
	tag.append(linha[1])
	
#print find_le(conteudo,'20170113153016356')

print find_ge(data, sys.argv[1])
print find_le(data, sys.argv[2])


print len(sys.argv)

inputTxt.close()
outputTxt.close()
