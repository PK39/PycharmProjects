import random, sys, transpositiondecrypt, transpositionencrypt

def main():
    random.seed(42)

    for i in range(200):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random. randint(4, 40)

        message = list(message)

        random.shuffle(message)
        message = ''.join(message)

        print('Test #%s: "%s..."' % (i + 1, message[:40]))

        for key in range(1, int(len(message)/2)):
            encrypted = transpositionencrypt.encryptMessage(key, message)
            decrypted = transpositiondecrypt.decryptMessage(key, encrypted)


        if message != decrypted:
            print('Mismatch with key %s and message %s.' % (key, message))
            print('Decrypted as: ' + decrypted)
            sys.exit()

    print('Transposition cipher test passed.')

if __name__ == '__main__':
    main()