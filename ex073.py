times = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 
        'Corinthians', 'Athletico-PR', 'Atlético-MG', 'América-MG', 
        'Fortaleza', 'São Paulo', 'Botafogo', 'Santos', 
        'Bragantino', 'Goiás', 'Coritiba', 'Ceará',
        'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')
print('-'*15)
print(f'Lista de times do brasileirão: {times}')
print('-'*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-'*15)
print(f'Os 4 últimos são {times[-4:]}')
print('-'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-'*15)
print(f'O Palmeiras está na {times.index("Palmeiras")+1}ª posição')