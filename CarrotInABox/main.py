"""Carrot in a Box"""

import random

print('''Carrot in a Box''')

input("Press enter to begin...")

p1Name = input('Human player 1, enter your name: ')
p2Name = input('Human player 2, enter your name: ')
playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)

print(''' Here are two boxes
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/''')

print()
print(playerNames)
print(p1Name + ', you have a RED box in front of you.')
print(p2Name + ', you have a GOLD box in front of you.')

print(p1Name + ', you will get to look into your box.')
print(p2Name.upper() + ', close your eyes and don\'t look!!!')
input('When ' + p2Name + 'has closed their eyes, press Enter...')

print(p1Name + ' here is the inside of your box:')

if random.randint(1, 2,) == 1:
    carrotInFirstBox = True
else:
    carrInFirstBox = False

if carrotInFirstBox:
    print('''
    ___VV____
    | VV |
    | VV |
  |___||____|   __________
 /    ||   /|  /         /|
+---------+ | +---------+ |
|   RED   | | | GOLD    | |
|   BOX   | / | BOX     | /
+---------+/  +---------+/
 (carrot!)''')
    print(playerNames)
else:
    print('''
   _________
  |         |
  |         |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
| RED     | |  | GOLD    | |
| BOX     | /  | BOX     | /
+---------+/   +---------+/    
(no carrot!)''')
    print(playerNames)

input('Press Enter to continue...')

print('Press Enter to continue...')

print('\n' * 100)
print(p1Name + ', tell ' + p2Name + ' to open their eyes.')
input('Press Enter to continue...')

print(p1Name + ', say one of the follwing sentences to ' +p2Name + '.')
print(' 1) There is a carrot in my box.')
print(' 2) There is not a carrot in my box.')

input('Then press Enter to continue...')

print(p2Name + ', do you want to swap boxes with ' + p1Name + '? YES/NO')
while True:
    response = input('> ').upper()
    if not (response.startswith('Y') or response.startswith('N')):
        print(p2Name + ', please enter "YES" or "NO".')
    else:
        break
firstBox = 'RED '
secondBox = 'GOLD'

if response.startswith('Y'):
    carrInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox, firstBox

print('''Here are the two boxes:
    ''')