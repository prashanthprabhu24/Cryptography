import time
import os
import sys
import transpositionEncrypt
import transpositionDecrypt


def main():
    print('Enter a file path/name (.txt) to encrypt/decrypt')
    inputFilename = input('> ')
    outputFilename = inputFilename + '.encrypted.txt'
    print('Enter the Encryption/Decryption Key')
    mykey = int(input('> '))
    print('Enter (E)ncryption or (D)ecryption mode?')
    myMode = input('> ')[0].lower()

    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % inputFilename)
        sys.exit()
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % outputFilename)
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
    print('%sing...' % (myMode.title()))
    startTime = time.time()
    translated = 'Process Not Found...'
    if myMode == 'e':
        myMode = 'Encrypt'
        translated = transpositionEncrypt.encryptMessage(mykey, content)
    elif myMode == 'd':
        myMode = 'Decrypt'
        translated = transpositionDecrypt.decryptMessage(mykey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time : %s seconds' % (myMode.title(), totalTime))
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()
    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


if __name__ == '__main__':
    main()
