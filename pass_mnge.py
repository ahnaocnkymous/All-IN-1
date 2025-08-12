print("I'm gonna be the King of the Hackers/Programmer!\nI'm gonna surpass my limits right here, right now~")
from cryptography.fernet import Fernet

# Add master password thing later on...
'''
def write_key(): # Encryption
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
        '''

# write_key()

def load_key(): # Decryption
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key

# master_pwd = input("What's the Master Password? ")
key = load_key() 
fer = Fernet(key)

def view():
    with open('password.txt','r') as file:
        for line in file:
            parts = line.strip().split('|') # this parts var [the sentence is remove "spaces & newlines" by. strip()] and split divide the sentence into 2 parts or many parts where '|' is appears
            if len(parts) != 2: 
                continue  # skip bad lines
            name = parts[0]
            encrypted = parts[1]
            password = fer.decrypt(encrypted.encode()).decode()
            print(name, ":", password)

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()  # decode to string
    

    with open('password.txt','a') as f:
        f.write(f"Account Name: {name} | Password: {encrypted_pwd}\n")


while True:
    mode = input('Would you like to add a new password or view existing ones (view,add), press q to quit?  ')
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid Mode.')
        continue
