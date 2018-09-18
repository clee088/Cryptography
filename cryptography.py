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
        if i == 'e':
            msg = input('Message: ')
            key = input('Key: ')
            p = ''
            kk = ''
            kk += key
            for l in msg:
                x = associations.find(l)
                if len(msg) > len(kk):
                    while True:
                        kk += key
                        if len(kk) > len(msg):
                            break
                    for k in kk:
                        y = associations.find(k)
                else:
                    for k in key:
                        y = associations.find(k)
                        
                xy = associations[x+associations.find(k)]
                #if xy > len(associations):
                p += str(xy)
            print(p)
            prompt()
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
        elif i == 'q':
            print('Goodbye!')
        else:
            print('Did not understand command, try again.')
            prompt()
prompt()