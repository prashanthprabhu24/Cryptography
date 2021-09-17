import random
import sys
import transpositionEncrypt
import transpositionDecrypt


def main():
    random.seed(42)
    for i in range(200):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Text #%s: "%s..."' % (i + 1, message[:50]))

        for key in range(1, len(message)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print(decrypted)
                sys.exit()
    print('Transposition cipher test passed.')


if __name__ == '__main__':
    main()
