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
# for i in range([2]):
#     print('i = ',i)

# 6.7

