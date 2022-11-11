resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
media = soma / quant
print(f'Você digitou {quant} número(s), a média foi {media:.2f}.')
print(f'O maior valor foi {maior}, o menor foi {menor}.')