from cgitb import text
from cryptography.fernet import Fernet
# showing no module named cryptography




master_password=input("What is the master password? ")


# def write_key():
#     key=Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)





# key + password + text to encrypt = random text
# random text + key + password =text to encrypt

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            # print(data)
            user, passw=data.split("|")
            # print(data.split("|"))
            print(f"user : {user} |password : {passw}")




def add():
    name=input("Account name: ")
    password=input("Password: ")
    with open('password.txt','a') as f:
        f.write(name + "|" + password + "\n")

while True:
    mode=input("Would you like to view the passwords or add a new password?(view/add).Press q to quit ").lower()
    if mode =="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode.")
        continue


