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
#Encrypt
        if i == 'e':
            msg = input('Message: ')
            key = input('Key: ')
            p = '' #print
            kk = ''
            kk += key
            if len(msg) > len(key):
                    while True:
                        kk += key
                        if len(kk) >= len(msg):
                            break
            for l in msg:
                x = associations.find(l)
                for k in key:
                    y = associations.find(k)
                    xy = x+y
                if xy > len(associations):
                    xy = associations[xy - len(associations)]
                print(xy)
                p += associations[xy]
            print(p)
            prompt()
#Decrypt
        elif i == 'd':
            msg = input('Message: ')
            key = input('Key: ')
            p = ''
            for l in msg:
                x = associations.find(l)
                for k in key:
                    y = associations.find(k)
                xy = associations[x-associations.find(k)]
                p += str(xy)
            print(p)
            prompt()
#Quit
        elif i == 'q':
            print('Goodbye!')
#Invalid Input
        else:
            print('Did not understand command, try again.')
            prompt()
prompt()
