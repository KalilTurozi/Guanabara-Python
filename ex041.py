from datetime import date
atual= date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Compete pela categoria mirim.')
elif idade <= 14:
    print(f'Compete pela categoria infantil.')
elif idade <= 19:
    print(f'Compete pela categoria junior.')
elif idade <= 25:
    print(f'Compete pela categoria sênior.')
else:
    print(f'Compete pela categoria master.')        
