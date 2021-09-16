"""Caesar Cipher

    @Author: prashanthprabhu1998@gmail.com      Fri 05:00 AM IST, 7 SEPT 2021

    DESCRIPTION
        Caesar Cipher - Encryption and Decryption
        =====================

        Asks an user input message/code - of any length - and prints back code/plaintext with respect to the Input.
"""

Plain_Text = input('Enter The Plain Text/Cipher Text to encrypt/decrypt : ')
Key = int(input('Enter the Encryption/Decryption Key : '))

print('Type (E)ncrypt or (D)ecrypt')
Process = input('> ').title()[0]

val = None
Cipher_Text = ''
Plain_Text = Plain_Text.upper().split(' ')
for i in Plain_Text:
    for j in i:
        if Process == 'E':
            val = ord(j) + Key
            if val >= 91:
                val = val - 26
        elif Process == 'D':
            val = ord(j) - Key
            if val <= 64:
                val = val + 26
        Cipher_Text += chr(val)
    Cipher_Text += ' '
print(Cipher_Text)
