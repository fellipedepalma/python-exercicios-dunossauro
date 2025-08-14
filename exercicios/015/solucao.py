valor_hora = float(input('Digite o valor da sua hora trabalhada: '))
quantidade_horas_mes = int(input('Digite a quantidade de horas trabalhas no mês: '))
salario_bruto = valor_hora * quantidade_horas_mes
desconto_ir = salario_bruto * (11 / 100)
desconto_inss = salario_bruto * (8 / 100)
desconto_sindical = salario_bruto * (5 / 100)
descontos = desconto_ir + desconto_inss + desconto_sindical
print(f'+ Salário Bruto: R$ {salario_bruto:.2f}')
print(f'- IR (11%): R$ {desconto_ir:.2f}')
print(f'- INSS (8%): R$ {desconto_inss:.2f}')
print(f'- Sindicato  (5%): R$ {desconto_sindical:.2f}')
print(f'= Salário Líquido: R$ {salario_bruto - descontos}')
