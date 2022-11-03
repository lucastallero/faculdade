# # 6.2

# def ordenar():
#     numeros = input("Insira os três números")

#     n1 = numeros.split(' ')[0]
#     n2 = numeros.split(' ')[1]
#     n3 = numeros.split(' ')[2]

#     if n1 > n2:
#         if n2 > n3:
#             print(f"{n3}, {n2}, {n1}")
#         else:
#             print(f"{n2}, {n3}, {n1}")

#     elif n2 > n1:
#         if n1 > n3:
#             print(f"{n3}, {n1}, {n2}")
#         else:
#             print(f"{n1}, {n3}, {n2}")

#     else:
#         if n2 > n1:
#             print(f"{n1}, {n2}, {n3}")
#         else:
#             print(f"{n1}, {n2}, {n3}")

# ordenar()

# distancia = 120

# def A1():
#     custo_comb = 0.15
#     portagens = 6.52
#     custo_total = distancia * custo_comb + portagens
#     print(f"{custo_total:.2f}")

# def A20():
#     custo_comb = 0.12
#     portagens = 15.2
#     custo_total = distancia * custo_comb + portagens
#     print(f"{custo_total:.2f}")

# def A21():
#     custo_comb = 0.10
#     portagens = 5.75
#     custo_total = distancia * custo_comb + portagens
#     print(f"{custo_total:.2f}")

# rota = input("Digite a rota que deseja tomar:\n")
# rota = rota.upper()
# if rota == "A21":
#     A21()
# elif rota == "A20":
#     A20()
# elif rota == "A1":
#     A1()
# else:
#     print("Então que vá a pé!")

# 6.4

# renda_bruta = float(input("Digite seu rendimento bruto:"))

# def renda_liquida():
#     IRS = 0.25
#     SS = 0.05
#     CNA = 0.1
#     impostos = IRS + SS + CNA
#     calc_renda = renda_bruta - (renda_bruta * impostos)
#     print(calc_renda)

# renda_liquida()

# 6.5 

# def avaliação():
#     notas = input("Insira as notas:\n")

#     t1 = float(notas.split(' ')[0])
#     t2 = float(notas.split(' ')[1])
#     t3 = float(notas.split(' ')[2])
#     t4 = float(notas.split(' ')[3])
#     exame = float(notas.split(' ')[4])

#     nota_final = 0.0
#     nota_final = 0.075 * (t1+t2+t3+t4) + 0.7 * exame

#     if nota_final >= 14:
#         print('Aprovado!')
#     elif 7 <= nota_final < 14:
#         print('Oral!')
#     else:
#         print('Reprovado!') 

# avaliação()

# 6.6

# i = 20
# for i in range(20, -1, -2):
#     print(i)

# 6.7

# for i in range(3):
#     for j in range(1,3):
#         print(i/j)
        
# 6.8

def amigas():
    amiga1 = 'abcdefghijkl'
    amiga2 = 'ahwefgghijkl'
    j = 0.00
    pct = len(amiga1)/100

    for i in range(len(amiga1)):
        if amiga1[i] == amiga2[i]:
            j += pct
    
    if j > 0.9:
        print('Amigas')
    else:
        print('não são amigas')

# amigas()

# 6.9

import math

def smallest(numero):
    i = 0
    divisor = 2
    while i == 0:
        if numero % divisor == 0:
            i = 1
        else:
            divisor += 1
    print(f'O menor divisor de {numero} é {divisor}')

# # smallest(25)

def primo(numero):
    raiz_quadrada = math.sqrt(numero) + 1
    for divisor in range(2,int(raiz_quadrada)):
        if numero % divisor == 0:
            print(f"{numero} não é primo")
            return
        if divisor <= int(raiz_quadrada):
            print(f"{numero} é primo")
    
# primo(10)

import random

def dado(rodados):
    cont_impar = 0
    cont_par = 0
    for i in range(rodados):
        roll = random.randrange(1,7)
        if roll % 2 != 0:
            cont_impar += 1
        if roll % 2 == 0:
            cont_par += 1
    
    pct_par = (cont_par * 100)/rodados
    pct_impar = (cont_impar * 100)/rodados
    print(pct_impar, pct_par)

# dado(50000)

def factorial(n):
    resultado = 1
    for i in range(n):
        j = n-i
        resultado *= j

    print(resultado)

# factorial(5)