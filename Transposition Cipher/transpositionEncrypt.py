import pyperclip


def main():
    print('Type/Paste the Plain Text')
    myMessage = input('> ')
    print('Enter the Encryption Key')
    myKey = int(input('> '))
    cipherText = encryptMessage(myKey, myMessage)
    print(cipherText + '|')
    print()
    print('Copied to Clipboard...')
    pyperclip.copy(cipherText)


def encryptMessage(key, message):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)


if __name__ == '__main__':
    main()
