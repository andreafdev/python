salario = float(input('Informe seu salário: '))

if salario <= 3000:
    print('Você é um programador júnior.')
elif salario > 3000 and salario <= 6000:
    print('Você é um programador pleno.')
elif salario > 6000 and salario <= 15000:
    print('Você é um programador sênior.')
else:
    print('Gerente de projetos.')
