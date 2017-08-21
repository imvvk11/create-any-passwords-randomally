import random  #imports random module

def password(length):
    length = int(input("Provide length of your password: "))
    pw = str()
    characters = "abcdefghijklmnopqrstuvwxyz0123456789@#!*&%$"
    
    for i in range(length):
        pw = pw + random.choice(characters)
    return pw

#test cases
#password(8)
#password(10)
