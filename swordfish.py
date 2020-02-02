while True:
    print('what is your name?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. what password you would like to enter.')
    password = input()
    if password == 'swordfish':
        #break
        print('Access granted.')
