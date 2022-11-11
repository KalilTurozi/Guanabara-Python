casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end= ' ')
print(f'a prestação será de R${prestação:.2f}')
if prestação <= minimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo negado!')
