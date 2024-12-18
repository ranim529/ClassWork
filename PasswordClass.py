import random

class Password:
    def __init__(self, length=12):
        self.length = length
    def random_password(self):
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=<>?"
        password = ''.join(random.choice(char) for _ in range(self.length))
        return password
    def password_number(self, count):
        passwords = [self.random_password() for _ in range(count)]
        return passwords

print("give the length of your password:")
length = int(input())
print("how many password you want?")
count = int(input())

password_generator = Password(length)
passwords = password_generator.password_number(count)

for i, pwd in enumerate(passwords, 1):
    print(pwd)
