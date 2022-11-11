from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    opção = int(input('>>>>> Qual é sua opção? '))
    if opção == 1:
            soma = v1 + v2
            print(f'A soma entre {v1} + {v2} é {soma}')
    elif opção == 2:
        produto = v1 * v2
        print(f'O resultado de {v1} x {v2} é {produto}')
    elif opção == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print(f'Entre {v1} e {v2}, o maior valor é {maior}')
    elif opção == 4:
        print('Informe os números novamente: ')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('---' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')