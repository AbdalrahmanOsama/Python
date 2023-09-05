master_password = input('Enter The Master Password: ')


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line)


def add():
    account = input('Account Name: ')
    password = input('Account Password: ')
    with open('passwords.txt', 'a') as f:
        f.write(account + "|" + password + "\n")


def encrypt():
    pass


def decrypt():
    pass





while True:
    mode = input('Would You Like To Add a New Password or View Existing Ones? ').lower()
    if mode == "view":
        pass
    elif mode == "add":
        pass
    elif mode == "q":
        break
    else:
        print('Invalid Mode.')
        continue


