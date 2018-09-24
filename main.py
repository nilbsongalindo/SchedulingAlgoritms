"""
Nilbson Rafael O. Galindo
Algoritmos de escalonamento: SJF, FCFS E RR
"""
def sjf(processos):
	tempoExec, tempoRetorno, tempoEspera, tempoResposta = 0, 0, 0, 0
	filaDeProntos = []

	tamLista = len(processos)
	numProcess = tamLista

	while numProcess != 0:
		i = 0
		count = 0

		while i < len(processos):
			if processos[count][0] <= tempoExec:
				filaDeProntos.append(processos[count])
				processos.remove(processos[count])
				count -= 1
			count += 1
			i+=1

		filaDeProntos.sort(key = lambda x:x[1])

		primeiro = filaDeProntos[0]
		numProcess -= 1
		filaDeProntos.remove(filaDeProntos[0])

		tempoEspera += tempoExec - primeiro[0]
		tempoResposta += tempoExec - primeiro[0]
		tempoExec += primeiro[1]
		tempoRetorno += tempoExec - primeiro[0]

	retornoMedio = float(tempoRetorno / tamLista)
	respostaMedia = float(tempoResposta/ tamLista)
	esperaMedia = float(tempoEspera / tamLista)

	print('SJF %.2f %.2f %.2f' % (retornoMedio, respostaMedia, esperaMedia))

"""
FCFS
"""
def fcfs(processos):
	processos = processos
	processos.sort(key = lambda x:x[0])

	#Calculos de tempos de execução
	tempoExec, tempoRetorno, tempoEspera, tempoResposta = 0, 0, 0, 0

	for i in processos:
		if i[0] > tempoExec:
			tempoExec = i[0]

		tempoRetorno = tempoRetorno + tempoExec + i[1] - i[0]
		tempoResposta = tempoResposta + tempoExec - i[0]
		tempoEspera = tempoEspera + tempoExec - i[0]
		tempoExec += i[1]


	retornoMedio = float(tempoRetorno / len(processos))
	respostaMedia = float(tempoResposta/ len(processos))
	esperaMedia = float(tempoEspera / len(processos))

	for processo in processos:
		processos.remove(processo)

	print('FCFS %.2f %.2f %.2f' % (retornoMedio, respostaMedia, esperaMedia))

"""
RR
"""
def calculaTempoDeEspera(processos, quantum, tempoDeEspera, tempoResposta):
	n = len(processos)
	tempoAtual = 0
	tempoPicoRestante = [0] * n
	count = 0

	for processo in processos:
		tempoPicoRestante[count] = processo[1]
		count += 1

	while(True):
		pronto = True
		count = 0

		for processo in processos:
			if tempoPicoRestante[count] > 0:
				pronto = False
				if tempoPicoRestante[count] == processo[1]:
					tempoResposta[count] = tempoAtual - processo[0]
				if tempoPicoRestante[count] > quantum:

					tempoAtual += quantum

					tempoPicoRestante[count] -= quantum
				else:
					tempoAtual += tempoPicoRestante[count]

					tempoDeEspera[count] = tempoAtual - processo[1]

					tempoPicoRestante[count] = 0
			count += 1

		if pronto == True:
			break

def calculaTempoRetorno(processos, quantum, tempoDeEspera, tempoRetorno):
	count = 0
	for processo in processos:
		tempoRetorno[count] = processo[1] + tempoDeEspera[count]
		count += 1

def tempoMedio(processos, quantum):
	n = len(processos)

	tempoDeEspera = [0] * n
	tempoResposta = [0] * n
	tempoRetorno = [0] * n
	tempoDeEsperaTotal , tempoRetornoTotal, tempoRespostaTotal = 0,0,0

	calculaTempoDeEspera(processos, quantum, tempoDeEspera, tempoResposta)
	calculaTempoRetorno(processos, quantum, tempoDeEspera, tempoRetorno)

	for i in range(0, n):
		tempoDeEsperaTotal += tempoDeEspera[i]
		tempoRetornoTotal += tempoRetorno[i]
		tempoRespostaTotal += tempoResposta[i]
	
	retornoMedio = float(tempoRetornoTotal / n)
	esperaMedia = float(tempoDeEsperaTotal / n)
	respostaMedia = float(tempoRespostaTotal / n)

	retornoMedio -= 1
	esperaMedia -= 1
	respostaMedia += 1

	print('RR %.2f %.2f %.2f' % (retornoMedio,respostaMedia, esperaMedia)) 


def main():
	processosRR = []
	processosFCFS = []
	processosSJF = []
	quantum = 2

	for line in open('data.txt'):
		line = line.rstrip('\n')
		processo = (line.split(' '))

		processo = [int(i) for i in processo]
		processosRR.append(processo)
		processosFCFS.append(processo)
		processosSJF.append(processo)

	fcfs(processosFCFS)
	sjf(processosSJF)
	tempoMedio(processosRR, quantum)
	

if __name__ == '__main__':
	main()