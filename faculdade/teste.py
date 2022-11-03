def preco_viagem(estrada):
    if estrada == 'A1':
        preco_viagem = 120*0.15+6.52
    if estrada == 'A20':
        preco_viagem == 120*0.12+15.2
    if estrada == 'A21':
        preco_viagem = 120*0.10+5.75
    
if __name__ == '__main__':
    estrada = 'A1'
    preco_viagem(estrada)
    print(preco_viagem(estrada))