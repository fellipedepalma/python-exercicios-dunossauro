peso = float(input('Digite a quantidade dos KGs: '))
limite_peso = 50.00
valor_kg_excedido = 4.00

if peso > limite_peso:
    excesso = peso - limite_peso
    valor_multa = excesso * valor_kg_excedido
    print(f'Você excedeu {excesso:.2f}Kg e deve pagar uma multa de R$ {valor_multa:.2f}')
else:
    print(f'Você pescou dentro do limite estabelecido.')
