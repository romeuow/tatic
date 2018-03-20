# teste_buscador.py

import pytest
import subprocess
import constantes


def teste_nenhum_registro():
	subprocess.call("python buscador.py" + " 20140101000004398 20140101000031476", shell=True)
	inputTxt = open(constantes.RESULTADO,'r')
	assert len(inputTxt.read()) == 0
	inputTxt.close()

#Pesquisa tres tags em todo range de datas do arquivo de exemplo
def teste_tres_eventos():
	subprocess.call("python buscador.py" + " 20170101000004398 20170227235957419 0A71C55C 0AD4C55D 0A410D47", shell=True)
	inputTxt = open(constantes.RESULTADO,'r')
	registro = []
	for linha in inputTxt:
		registro.append(linha)
	assert len(registro) == 8
	inputTxt.close()

teste_nenhum_registro()
teste_tres_eventos()