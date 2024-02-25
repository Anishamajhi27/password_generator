import string
import random

charvalues = string.ascii_letters 
num = string.digits
pancuation = string.punctuation

pass_len = int(input('enter password length: '))

password = "".join([random.choice(charvalues) for i in range(pass_len-2)])
password = password + random.choice(num) +random.choice(pancuation)
print(password)
