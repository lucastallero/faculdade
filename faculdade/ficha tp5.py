import math

# # 5.2

# a, b, c = input().split(' ') # # Entrada e assigning variáveis

# a = int(a)
# b = int(b)
# c = int(c)

# s = (a + b + c) / 2 # # Cálculo

# area = math.sqrt(s*(s-a)*(s-b)*(s-c))

# print(area)


# # 5.3


# alt, graus = input().split()

# alt = int(alt)
# graus = int(graus)

# radianos = (math.pi/180)*graus
# comp = alt/math.sin(radianos)

# print(comp)


# # 5.4


# def bpm():
#     idade = float(input())

#     bpm_medio = 163 + (1.16*idade) - (0.018*(idade ** 2))
#     print(bpm_medio)

# bpm()


# # 5.5


# def juros():
#     valor_inicial = 2000
#     taxa_juros = 0.0125
#     anos_decorridos = 0
#     montante = int()

#     while (montante < valor_inicial * 2):
#         anos_decorridos += 1
#         montante = valor_inicial * ((1 + taxa_juros) ** anos_decorridos)


#     print(anos_decorridos)

# juros()


# # 5.6

# # Acredite se quiser, essa merda está certa, 
# # é pra render o mesmo tanto por ano só que por mês. 
# # Por que isso existe? Nem Deus sabe. Isso é uma abominação. 
# # Eu estou puto, muito triste e 
# # desapontado com a existência dessa sujeira permitida por Deus.

# def juros():
#     valor_inicial = 2000
#     rendimento = 12
#     duracao_anos = float(input("Quantos anos durará seu investimento?\n"))
#     composicao = float(rendimento * duracao_anos)
#     taxa_juros = 0.0125

#     montante = valor_inicial * (1 + taxa_juros / rendimento) ** composicao


#     print(f"Após {duracao_anos} anos, seu investimento valerá {montante}")

# juros()

# # 5.7

# # 5.8

# # 5.9

# # 5.14

# def subcadeia():
#     i = 0
#     frase = input("Digite a frase:\n")
#     qtd = int(input("Digite o comprimento:\n"))

#     while qtd <= len(frase): # Enquanto houver pelo menos 3 caracteres até o fim da string
#         print(f"{frase[i:qtd]}") # Printa o fatiamento da frase
#         i += 1 # Avança um no index
#         qtd += 1 # Avança o fim do fatiamento em um no index
    
# subcadeia()

# # 5.15

# def prefixo():
#     frase = input("Digite a frase:\n")

#     for i in range(len(frase) + 1):
#         print(f"{frase[0:i]}")
    
# prefixo()

# # 5.16

# def sufixo():
#     frase = input("Digite a frase:\n")

#     for i in range(len(frase) + 1):
#         print(f"{frase[len(frase)-1-i:len(frase)-1]}") # Começa no fim da string menos i, que muda com cada iteração e termina no fim da string

    
# sufixo()

# # 5.17, 5.18, 5.19

# import turtle
# import random

# taruga = turtle.Turtle()

#   ADN_taruga(tamanho = 200):
    
#     # Gerando uma string aleatória referente ao código genético
#     letras = ['f', 't', 'e', 'd']
#     cod_genetico = random.choices(letras, k = tamanho)

#     # Iterando e lendo a string, e então executando a ordem referente a letra indicada.
#     for i in range(0, len(cod_genetico)):
#         if cod_genetico[i] == 'f':
#             turtle.fd(random.randrange(0,30))
#         elif cod_genetico[i] == 't':
#             turtle.backward(random.randrange(0,30))
#         elif cod_genetico[i] == 'e':
#             turtle.lt(random.randrange(0,360))
#         elif cod_genetico[i] == 'd':
#             turtle.rt(random.randrange(0,360))

# ADN_taruga()

# 5.20

# def codigo():