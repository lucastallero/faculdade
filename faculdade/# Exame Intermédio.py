# Exame Intermédio

# Pergunta 1
# A) Um objeto tuplo é uma lista que leva apenas dois valores e é imutável.

# B) A função return para a execução da função ao ser executada, enquanto que a função print apenas retorna no terminal o que for pedido dentro da função,
# sem parar a execução da função.

# C) Um objeto ser imutável significa que, uma vez definidos, os valores inseridos neste objeto não podem ser alterados, seja adicionando/removendo objetos
# ou alterando objetos já presentes.


# Pergunta 2
# A) Em ordem: foi atribuído ao objeto de nome "x" o valor x, então foi definida a função "teste" com o parâmetro "y" que, ao ser executada, retorna y².
# Então, foi atríbuido à variável y o nome de x (4) e, logo em seguida, reatribuído para y + 1 (5). Pediu-se o ID (a localização na memória) de y, e então
# executou a função "teste" que retornou o valor 5² = 25. Checou então se o ID de x era igual o ID de y, que é falso, uma vez que tem valores diferentes 
# e, consequentemente, posições diferentes na memória.
# Ao final:
# x = 4
# y = 5

# B)
# def misterio(seq):
#     res = str()
#     for x in seq:
#         if x not in res:
#             res = res + x
#     return res

# é uma função que remove caracteres duplicados de uma string.

# Pergunta 3 (último)

# def pergunta3(num1, num2):
#     if num1 % 2 != 0 and num2 % 2 != 0:
#         return num1 + num2
#     else:
#         return abs(num1 - num2)

# Pergunta 3 (primeiro)

# def complementar():
#     cadeia1 = ['A', 'C', 'G', 'T', 'A']
#     cadeia2 = ['T', 'G', 'C', 'A', 'T'] 
#     for i in range(len(cadeia1)):
#         if (cadeia1[i] == 'A' and cadeia2[i] == 'T') or (cadeia1[i] == 'T' and cadeia2[i] == 'A') or (cadeia1[i] == 'C' and cadeia2[i] == 'G') or (cadeia1[i] == 'G' and cadeia2[i] == 'C'):
#             print("True")
#         else:
#             print('False')

# complementar()

# Pergunta 3 (segundo)

# def cadeia(c1, c2):
#     j = 0
#     k = -1
#     cadeia_r = str()
#     for i in range(len(c1) + len(c2)):
#         if i % 2 == 0:
#             cadeia_r += c1[j]
#             j += 1
#         elif i % 2 != 0:
#             cadeia_r += c2[k]
#             k -= 1
#     print(cadeia_r)
    
# cadeia('abc', 'DEF')

# Pergunta 3 (terceiro)

# def soma_ponto(cte, coord):
#     nova_coord = tuple()
#     for xn in coord:
#         novo_valor = cte + xn
#         nova_coord = nova_coord + (novo_valor,)
#     print(nova_coord)

# soma_ponto(3, (1,2,3,4))

# ponto(2)

# Pergunta 4A

# def encontrar(cadeia, encontrar):
#     posicao = 0
#     for caractere in encontrar:
#         index = cadeia.find(caractere, posicao)
#         if index == -1:
#             return False
#         else:
#             posicao = index + 1
#     return True

# Pergunta 4B

# def equilibrio(ADN):
#     count_A = ADN.count('A')
#     count_T = ADN.count('T')
#     count_C = ADN.count('C')
#     count_G = ADN.count('G')
#     if (count_A + count_T) == (count_C + count_G):
#         return True
#     else:
#         return False

# Pergunta 4C

# def ligacao(ordem, string_contida, string_grande):

# Pergunta 5A

import turtle


# taruga = turtle.Turtle()
# def nautilus(set_x, set_y, cor, orient, tamanho): # Int, Int, Int, String, Int
    
#     # Posição inicial
#     taruga.up()
#     taruga.setpos(set_x,set_y)
#     taruga.down()

#     # Cor
#     taruga.pencolor(cor)

#     # Orientação
#     taruga.seth(orient)

#     for i in range(25):
#         for i in range(5):
#             taruga.fd(tamanho)
#             taruga.rt(72)
#         tamanho = tamanho * 0.94
#         taruga.rt(20)

# nautilus(0,0,'blue', 270, 100)


# Pergunta 5B

# turtle.speed(10)
# for i in range (12):
#     for n in range(2):
#         turtle.left(60)
#         turtle.forward(100)
#         turtle.left(60)
#         turtle.forward(100)
#         turtle.left(60)
#     turtle.rt(30)

# turtle.done()

# Pergunta 5C

# taruga = turtle.Turtle()

# def estrela():
#     for i in range(5):
#         taruga.fd(100)
#         taruga.lt(50)
#         taruga.fd(100)
#         taruga.rt(122)

# estrela()

# turtle.done()