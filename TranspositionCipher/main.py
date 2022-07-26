import pyperclip

def main():
    myMessage = 'Common sense is not so common but it is very common.'
    myKey = 8
#    minKey = int(len(myMessage)-(len(myMessage)-2)) # Min key atleast 2
    minKey = 2
    maxKey = int(len(myMessage)/2)

    for x in range(minKey, maxKey):
        print(x)


    ciphertext = encryptMessage(myKey, myMessage)
#    ciphertext2 = loopencrypt(myKey, myMessage)

#    for x in range(2, maxKey)
#        ciphertextlooped = encryptMessage()

    print("Maxkey: ",maxKey,"\nMinkey: ",minKey)
    print(ciphertext + '|')
#    print(key1)

    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    ciphertext = [''] * key
    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]

            currentIndex += key

    return ''.join(ciphertext)
'''
def loopencrypt(key1, message):

    ciphertext = [''] * key
    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]

            currentIndex += key

    return ''.join(ciphertext)
'''





if __name__ == '__main__':
    main()