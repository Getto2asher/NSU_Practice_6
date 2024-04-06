place = input()

r = ['a', 'c', 'e', 'g']
l = ['b', 'd', 'f', 'h']
num = int(place[-1])
letter = place[0]

if letter in r:
    if num % 2 != 0:
        print('Чёрный')
    else:
        print('Белый')
elif letter in l:
    if num % 2 != 0:
        print('Белый')
    else:
        print('Чёрный')