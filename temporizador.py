import time

t = input('Digite o tempo em segundos: ')

if t.isdigit():
    t = int(t)
else:
    print('Informe um valor numérico')
    quit()

while t != 0:
    minutes, seconds = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    print(f'\r{timer}', end='')
    time.sleep(1)
    t = t - 1

print('\nO tempo acabou!')


