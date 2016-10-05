#!/usr/bin/python
import json
import sys


class Elevador:
    def __init__(self, andar_inicial, passo):
        self.andar_inicial = andar_inicial
        self.passo = passo
        self.andar_maximo = None

    def __str__(self):
        return 'Andar inicial: %d, ' \
               'Passo: %d, ' \
               'Andar maximo %d' % \
               (self.andar_inicial, self.passo, self.andar_maximo)

    def calcula_andar_maximo(self):
        temp = altura_torre - self.andar_inicial
        temp = temp / self.passo
        self.andar_maximo = temp * self.passo + self.andar_inicial


def adiciona_ligacao(andar1, andar2):
    if andar1 not in grafo:
        grafo[andar1] = [andar2]
    else:
        grafo[andar1].append(andar2)

grafo = {}


# Le dados iniciais
linhas_do_arquivo = []
print "---------"
print sys.argv[1]
with open(sys.argv[1], 'r') as file:
    linhas_do_arquivo = file.read()
    linhas_do_arquivo = linhas_do_arquivo.split('\n')

primeira_linha = linhas_do_arquivo.pop(0).split(' ')
altura_torre = int(primeira_linha[0])
quantidade_elevadores = int(primeira_linha[1])

segunda_linha = linhas_do_arquivo.pop(0).split(' ')
inicio = int(segunda_linha[0])
fim = int(segunda_linha[1])


# Cria os elevadores para posteriormente criar o grafo
elevadores = [None] * quantidade_elevadores
for i in range(0, quantidade_elevadores):
    linha_atual = linhas_do_arquivo[i].split(' ')
    elevadores[i] = Elevador(int(linha_atual[0]), int(linha_atual[1]))
    elevadores[i].calcula_andar_maximo()


# Gera o grafo em memoria
for elevador_atual in elevadores:
    andar_atual = elevador_atual.andar_inicial
    passo_atual = elevador_atual.passo
    proximo_andar = andar_atual + passo_atual
    while proximo_andar < altura_torre:
        adiciona_ligacao(andar_atual, proximo_andar)
        adiciona_ligacao(proximo_andar, andar_atual)
        andar_atual = proximo_andar
        proximo_andar = proximo_andar + passo_atual

if inicio not in grafo:
    print "Erro: nao existe o andar inicial %d" % (inicio)
    sys.exit(0)
if fim not in grafo:
    print "Erro: nao existe o andar final %d" % (fim)
    sys.exit(0)


# Comeca a percorrer o grafo
andar_atual = inicio
andar_final = fim
pilha_andares_para_retornar = []
caminho_percorrido = [andar_atual]
while andar_atual != andar_final:
    if len(grafo[andar_atual]) > 1:
        pilha_andares_para_retornar.append(andar_atual)
    if len(grafo[andar_atual]) == 0:
        del grafo[andar_atual]
        if len(pilha_andares_para_retornar) > 0:
            andar_atual = pilha_andares_para_retornar.pop()
        else:
            print 'Nao ha caminho de %d ate %d' % (inicio, fim)
            print caminho_percorrido
            sys.exit(0)

        ultimo_nodo_percorrido = caminho_percorrido.pop()
        while andar_atual != ultimo_nodo_percorrido:
            ultimo_nodo_percorrido = caminho_percorrido.pop()
        caminho_percorrido.append(ultimo_nodo_percorrido)

        continue

    proximo_andar = grafo[andar_atual].pop(0)
    # if len(grafo[andar_atual]) == 0:
    #     del grafo[andar_atual]

    grafo[proximo_andar].remove(andar_atual)
    andar_atual = proximo_andar
    caminho_percorrido.append(andar_atual)

#print json.dumps(grafo, indent=4)
#print caminho_percorrido
