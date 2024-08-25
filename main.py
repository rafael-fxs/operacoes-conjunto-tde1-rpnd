# Aluno: Rafael Felipe Xavier da Silva
# Curso: 6 Período BSI
# Matéria: Resolução de Problemas de Natureza Discreta

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

def ler_arquivo(caminho):
    try:
        caminho = caminho if caminho.endswith(".txt") else caminho + ".txt"
        with open(caminho, "r") as arquivo:
           return arquivo.readlines()
    except FileNotFoundError:
        print("Não foi possível encontrar o arquivo!")
        exit()
        
def processar_operacoes(linhas):
    total_operacoes = int(linhas[0])
    linhas = linhas[1:]
    for i in range(total_operacoes):
        index = i * 3
        tipo = linhas[index].strip()
        a = limpar_converter(linhas[index + 1])
        b = limpar_converter(linhas[index + 2])
        executar_operacao(tipo, a, b)
    
def limpar_converter(lista):
    resultado = []
    for item in lista.split(','):
        item = item.strip()
        if item.isdigit():
            resultado.append(int(item)) 
        elif '.' in item:
            resultado.append(float(item)) 
        else:
            resultado.append(item)
    return resultado
        
def executar_operacao(tipo, a, b):
    match tipo:
        case "U":
            efetuar_uniao(a, b)
        case "I":
            efetuar_intersecao(a, b)
        case "D":
            efetuar_diferenca(a, b)
        case "C":
            efetuar_produto_cartesiano(a, b)
        case _:
            print("Tipo de operação desconhecido.")
            
def efetuar_uniao(a, b):
    resultado = remover_duplicados(a + b)
    imprimir_resultado("União", a, b, resultado)
    
def efetuar_intersecao(a, b):
    resultado = remover_duplicados([elemento for elemento in a if elemento in b])
    imprimir_resultado("Interseção", a, b, resultado)
    
def efetuar_diferenca(a, b):
    resultado = remover_duplicados([elemento for elemento in a if elemento not in b])
    imprimir_resultado("Diferença", a, b, resultado)
    
def efetuar_produto_cartesiano(a, b):
    resultado = remover_duplicados([(x, y) for x in a for y in b])
    imprimir_resultado("Produto Cartesiano", a, b, resultado)
    
def remover_duplicados(lista):
    return list(dict.fromkeys(lista))
    
def imprimir_resultado(tipo, a , b, resultado):
    print(f"{tipo}: conjunto 1 {formatar_conjunto(a)}, conjunto 2 {formatar_conjunto(b)}. Resultado: {formatar_conjunto(resultado)}".replace("'", ""))

def formatar_conjunto(conjunto):
    if not conjunto:
        return {}
    if isinstance(next(iter(conjunto)), tuple):
        return '{' + ', '.join(str(tupla) for tupla in conjunto) + '}'
    else:
        return '{' + ', '.join(map(str, conjunto)) + '}' 
           
arquivo = input("Digite o nome do arquivo para leitura: ")
linhas_arquivo = ler_arquivo(arquivo)
processar_operacoes(linhas_arquivo)