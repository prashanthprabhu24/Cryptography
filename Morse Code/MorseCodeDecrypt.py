"""Morse Code Decryption

    @Author: prashanthprabhu1998@gmail.com      Fri 02:00 AM IST, 7 SEPT 2021

    DESCRIPTION
        Morse Code Decryption
        =====================

        Asks an user input morse code - of any length - and prints back text message with respect to the Input
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
    ReverseMAP = {}
    for i in MAP:
        ReverseMAP[MAP[i]] = i
    return ReverseMAP


def main():
    print('Morse Code Decryption....')
    print('Type/Paste in Morse Code to convert to Plain Text')
    myMessage = input('> ')
    decrypted = decryptMorseCode(myMessage).replace('_','-')
    print('Decrypted!')
    print('Copied Decrypted code to Clipboard.')
    print()
    print(decrypted)
    print()
    print('*Truncated remaining messages*')
    pyperclip.copy(decrypted)


def decryptMorseCode(code):
    Map = mapping()
    # print(Map)
    text = ''
    code = code.replace('-','_').split()
    for i in code:
        if i in Map:
            text += Map[i]
        else:
            text += i
    return text


if __name__ == '__main__':
    main()
