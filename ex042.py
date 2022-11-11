l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM formar um triângulo', end=' ')
    if l1 == l2 == l3 == l1:
        print('EQUILÁTERO!')
    if l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')         

else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')    
