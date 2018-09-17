"""
cryptography.py
Author: Christopher Lee
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"


def prompt():
    ask = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    for i in ask:
        if i == 'e' or i == 'd' or i == 'q':
            msg = input('Message: ')
            key = input('Key: ')
            if len(msg) > len(key):
                for l in msg:
                    (associations.find(l) + associations.find(key))
            else:
                for l in msg:
                    ekey = (associations.find(l) + associations.find(key))
                for e in ekey:
                    k = associations[e]
                print(k)
        else:
            print('Did not understand command, try again.')
            prompt()
prompt()