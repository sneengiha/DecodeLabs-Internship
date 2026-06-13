import random
print("Password Generator")
size = int(input("How many characters do you want in the password? "))
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
new_password = ""
for i in range(size):
    new_password = new_password + random.choice(chars)
    print("Your password is:", new_password)