def main():
    print("Diamonds")

    for diamondSize in range(0, 6):
        displayOutlineDiamond(diamondSize)
        print()
        displayFilledDiamond(diamondSize)
        print()

def displayOutlineDiamond(size):
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/', end='')
        print(' ' * (i * 2), end='')
        print('\\')

    for i in range(size):
        print(' ' * i, end='')