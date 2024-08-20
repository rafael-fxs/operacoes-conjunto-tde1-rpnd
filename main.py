# Aluno: Rafael Felipe Xavier da Silva
# Curso: 6 Período BSI

# Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
# linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
# operações que serão realizadas entre dois conjuntos de dados.
# O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
# contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
# em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
# segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
# operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
# seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
# operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
# terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
# das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
# 4
# U
# 3, 5, 67, 7
# 1, 2, 3, 4
# I
# 1, 2, 3, 4, 5
# 4, 5
# D
# 1, A, C, 34
# A, C, D, 23
# C
# 3, 4, 5, 5, A, B, R
# 1, B, C, D, 1
# Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
# produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
# {𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
# A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
# dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
# a informação e a formatação mostrada a seguir:
# União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
# Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
# um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
# de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
# minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
# No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
# pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
# implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
# Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
# contendo um número diferente de operações, operações com dados diferentes, e operações em ordem
# diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no
# ambiente repl.it quanto no ambiente Github.
# Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com,
# no mínimo um arquivo de testes criado pelo próprio professor. 

linhas_arquivo = ""

def ler_arquivo(caminho):
    global linhas_arquivo
    try:
        with open(caminho, "r") as arquivo:
           linhas_arquivo = arquivo.readlines()
    except FileNotFoundError:
        print("Não foi possível encontrar o arquivo!")
        exit()
        
def processar_operacoes(linhas):
    total_operacoes = int(linhas[0])
    linhas = linhas[1:]
    for i in range(total_operacoes):
        index = i * 3
        tipo = linhas[index].strip()
        a = limpar_converter(linhas[index + 1].split(','))
        b = limpar_converter(linhas[index + 2].split(','))
        print(tipo)
        executar_operacao(tipo, a, b)
        
def executar_operacao(tipo, a, b):
    match tipo:
        case "U":
            operacao_uniao(a, b)
        case "I":
            operacao_intersecao(a, b)
        case "D":
            operacao_diferenca(a, b)
        case "C":
            operacao_uniao(a, b)
        case _:
            print("Tipo de operação desconhecido.")
            
def operacao_uniao(a, b):
    resultado = remove_duplicados(a + b)
    imprimir_resultado("União", a, b, resultado)
    
def operacao_intersecao(a, b):
    resultado = []
    for elementoA in a:
        for elementoB in b:
            if (elementoA == elementoB):
                resultado.append(elementoA)
    resultado = remove_duplicados(resultado)
    imprimir_resultado("Interseção", a, b, resultado)
    
def operacao_diferenca(a, b):
    resultado = []
    for elementoA in a:
        existe = False
        for elementoB in b:
            if (elementoA == elementoB):
                existe = True
                break
        if not existe:
            resultado.append(elementoA)
            
    resultado = remove_duplicados(resultado)
    imprimir_resultado("Diferenca", a, b, resultado)
    
def remove_duplicados(lista):
    return list(dict.fromkeys(lista))
    
def limpar_converter(lista):
    resultado = []
    for item in lista:
        item = item.strip()
        if item.isdigit():
            resultado.append(int(item)) 
        elif '.' in item:
            resultado.append(float(item)) 
        else:
            resultado.append(item)
    return resultado
    
def imprimir_resultado(tipo, a , b, resultado):
    print(f"{tipo}: conjunto 1 {set(a)}, conjunto 2 {set(b)}. Resultado: {set(resultado)} ")
        
print("####### TDE #######")
arquivo = input("Digite o nome do arquivo para leitura:\nObs: incluir o formato.\n")
ler_arquivo(arquivo)
processar_operacoes(linhas_arquivo)
