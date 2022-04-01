#make a program that is able to create a random password with both lowercase and uppercase letters numbers and symbols
import random
import string
import sys

def random_password(length):
    password = []
    for i in range(length):
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
    return ''.join(password)
#if -o is passed as an argument print the password into a pswd.txt file
#get lenght from input
if __name__ == '__main__':
    length = int(input("How long do you want your password to be? "))
    if len(sys.argv) == 2 and sys.argv[1] == '-o':
        with open('pswd.txt', 'w') as f:
            f.write(random_password(length))
    else:
        print(random_password(length))

