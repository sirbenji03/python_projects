from cryptography.fernet import Fernet


'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():  # real signature unknown
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("username:", user, "| password:",
                  fer.decrypt(passw.encode()).decode())


def add():  # real signature
    name = input("what is the Account Name? ")
    pwd = input("what is the password? ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "would you like to add a new password or view an aexisting password (view/add) or q to quit: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Unknown mode")
        continue
