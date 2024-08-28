valor_total = float(input('digite o valor do produto: '))
valor_disconto = valor_total 
valor_disconto -= (valor_total * 15/100)
print(f'preço total: {valor_total}, preço com disconto: {valor_disconto}')