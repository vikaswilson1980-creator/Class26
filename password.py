import random
import string
length = int(input("Enter the password length: "))
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
all_characters = list(lowercase + uppercase + numbers)
password = random.sample(all_characters, length)
random.shuffle(password)
final_password = ''.join(password)
print("Generated Password:", final_password)