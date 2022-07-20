import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
        print('''Bagels, a deductive logic game.\n
        I am thinking of a {}-digit number with no repeating
        digits.\n
        When I say:\tThat means:\n
        PICO\tOne digit is correct but in the wrong position.\n
        FERMI\tOne digit is correct and in the right position.\n
        BAGELS\tNo digit is correct.
        ''')

        while True:
            secretNum = getSecretNum()
            print('I have thought up the number.')
            print('You have {} guesses to get it.'.format(MAX_GUESSES))

            numGuesses = 1
            while numGuesses <= MAX_GUESSES:
                guess = ''
                while len(guess) != NUM_DIGITS or not guess.isdecimal():
                    print('Guess #{}: '.format(numGuesses))
                    guess = input ('> ')

                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

                if guess == secretNum:
                    break
                if numGuesses > MAX_GUESSES:
                    print('You ran out of guesses.')
                    print('The answer was {}.'.format(secretNum))

            print('Do you want to play again? (yes or no)')
            if not input('> ').lower().startwith('y'):
                break
        print('Thanks for playing!')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()

