"""Morse Code Encryption

    @Author: prashanthprabhu1998@gmail.com      Fri 02:00 AM IST, 7 SEPT 2021

    DESCRIPTION
        Morse Code Encryption
        =====================

        Asks an user input message - of any length - and prints back morse code with respect to the Input
        and copies to clipboard.
"""
import pyperclip


def mapping():
    MAP = {
        'A': '._',
        'B': '_...',
        'C': '_._.',
        'D': '_..',
        'E': '.',
        'F': '.._.',
        'G': '__.',
        'H': '....',
        'I': '..',
        'J': '.___',
        'K': '_._',
        'L': '._..',
        'M': '__',
        'N': '_.',
        'O': '___',
        'P': '.__.',
        'Q': '__._',
        'R': '._.',
        'S': '...',
        'T': '_',
        'U': '.._',
        'V': '..._',
        'W': '.__',
        'X': '_.._',
        'Y': '_.__',
        'Z': '__..',
        '.': '._._._',
        ',': '__..__',
        '?': '..__..',
        ' ': '/',
        '-':  '-....-',
        '/': '_.._.',
        '@': '.__._.',
        "'": '.----.',
        '1': '.____',
        '2': '..___',
        '3': '...__',
        '4': '...._',
        '5': '.....',
        '6': '_....',
        '7': '__...',
        '8': '___..',
        '9': '____.',
        '0': '_____'}
    return MAP


def main():
    print('Morse Code Encryption....')
    print('Type/Paste in message to convert to Morse Code')
    myMessage = input('> ')
    encrypted = encryptMorseCode(myMessage).replace('_','-')
    print('Encrypted!')
    print('Copied Encrypted code to Clipboard.')
    print()
    print(encrypted)
    print()
    print('*Truncated remaining code*')
    pyperclip.copy(encrypted)


def encryptMorseCode(text):
    Map = mapping()
    code = ''
    for i in text:
        if i.upper() in Map:
            code += Map[i.upper()] + ' '
        else:
            code += i
    return code


if __name__ == '__main__':
    main()
