"""Reverse Cipher Encryption/Decryption

    @Author: prashanthprabhu1998@gmail.com      Fri 04:00 AM IST, 7 SEPT 2021

    DESCRIPTION
        The Reverse Cipher encrypts a message by printing it in reverse order
        =====================================================================

        Asks an user input morse code - of any length - and prints back text message with respect to the Input
        and copies to clipboard.
"""
import pyperclip

def main():
    print('Type (E)ncrypt or (D)ecrypt')
    mode = input('> ').upper()
    if mode.upper().startswith('D'):
        data = reverseDecrypt()
    elif mode.upper().startswith('E'):
        data = reverseEncrypt()
    print(data[:100])
    print('Copied to clipboard!')
    pyperclip.copy(data)


def reverseDecrypt():
    print('Reverse Cipher Decryption...')
    print('Enter/Paste the code to Decrypt')
    message = input('> ')
    print('Decrypting...')
    print()
    return message[::-1]

def reverseEncrypt():
    print('Reverse Cipher Encryption...')
    print('Enter/Paste a Text/Message to Encrypt')
    message = input('> ')
    print('Decrypting...')
    print()
    return message[::-1]

if __name__ == '__main__':
    main()
