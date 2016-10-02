import json


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

grafo = {}

linhas_do_arquivo = []
with open('Teste.txt', 'r') as file:
    linhas_do_arquivo = file.read()
    linhas_do_arquivo = linhas_do_arquivo.split('\n')

primeira_linha = linhas_do_arquivo.pop(0).split(' ')
altura_torre = int(primeira_linha[0])
quantidade_elevadores = int(primeira_linha[1])

segunda_linha = linhas_do_arquivo.pop(0).split(' ')
inicio = int(segunda_linha[0])
fim = int(segunda_linha[1])

elevadores = [None] * quantidade_elevadores
for i in range(0, quantidade_elevadores):
    linha_atual = linhas_do_arquivo[i].split(' ')
    elevadores[i] = Elevador(int(linha_atual[0]), int(linha_atual[1]))
    elevadores[i].calcula_andar_maximo()


def adiciona_ligacao(andar1, andar2):
    if andar1 not in grafo:
        grafo[andar1] = [andar2]
    else:
        grafo[andar1].append(andar2)

for elevador_atual in elevadores:
    andar_atual = elevador_atual.andar_inicial
    passo_atual = elevador_atual.passo
    proximo_andar = andar_atual + passo_atual
    while proximo_andar < altura_torre:
        adiciona_ligacao(andar_atual, proximo_andar)
        adiciona_ligacao(proximo_andar, andar_atual)
        andar_atual = proximo_andar
        proximo_andar = proximo_andar + passo_atual

print json.dumps(grafo, indent=4)
