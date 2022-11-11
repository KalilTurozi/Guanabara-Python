soma  = cont = 0
while True:
    num = int(input('Digite um valor (999 pra parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma do(s) {cont} valor(es) foi {soma}')