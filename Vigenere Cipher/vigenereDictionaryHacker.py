import detectEnglish
import vigenereCipher
import pyperclip

def main():
    ciphertext = """LOL"""
    hackedMessage = hackVigenere(ciphertext)
    if hackedMessage != None:
        print('Copying hacked message to clipboard : ')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')

def hackVigenere(ciphertext):
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()
    for word in words:
        word = word.strip()
        decryptedText = vigenereCipher.decryptMessage(word,ciphertext)
        if detectEnglish.isEnglish(decryptedText,wordPercentage=85):
            print()
            print('Possible encryption break:')
            print('key '+str(word)+': '+decryptedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue')
            response = input('> ')
            if response.upper().startswith('D'):
                return decryptedText

if __name__ == '__main__':
    main()