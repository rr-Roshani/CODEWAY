import random
import string
print("Welcome to Password Generator")
def generate_password():
    length = int(input("Enter the length of Password that you would like to generate: "))
    lettersD=string.ascii_letters
    digitsD=string.digits
    symbolsD=string.punctuation
    combine=lettersD+digitsD+symbolsD
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    generate_password()
generate_password()