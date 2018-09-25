"""
cryptography.py
Author: Christopher Lee
Credit: https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list

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
            kk = ''
            if len(msg) > len(key):
                    while True:
                        kk += key
                        if len(kk) >= len(msg):
                            break
            m = [associations.find(l) for l in msg]
            k = [associations.find(k) for k in kk]
            mm = [m + k for m, k in zip(m, k)]
            p = ''.join([associations[i % len(associations)] for i in mm])
            print(p)
            prompt()
#Decrypt
        elif i == 'd':
            msg = input('Message: ')
            key = input('Key: ')
            kk = ''
            if len(msg) > len(key):
                    while True:
                        kk += key
                        if len(kk) >= len(msg):
                            break
            m = [associations.find(l) for l in msg]
            k = [associations.find(k) for k in kk]
            mm = [m - k for m, k in zip(m, k)]
            p = ''.join([associations[i % len(associations)] for i in mm])
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
