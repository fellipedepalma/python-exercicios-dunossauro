import math
m2_area = float(input('Insira a quantidade de m2 da área a ser pintada: '))
custo_lata18l = 80.00
rendimento_lata = 54.00
latas_necessarias = math.ceil(m2_area / rendimento_lata)
valor_total_venda = custo_lata18l * latas_necessarias
print(f'O cliente precisará de {latas_necessarias} latas')
print(f'O valor total dessa venda é de R$ {format(valor_total_venda, ".2f")}')
