def substituicao():
    cod_genetico = 'TCAGCT'
    cod_alternativo = str()

    for car in cod_genetico:
        if car == 'A':
            cod_alternativo += 'T'
        elif car == 'T':
            cod_alternativo += 'A'
        elif car == 'C':
            cod_alternativo += 'G'
        elif car == 'G':
            cod_alternativo += 'C'

    print(cod_alternativo)

substituicao()