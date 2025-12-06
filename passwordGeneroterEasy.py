import random
#Imports Python’s built-in random module, which allows us to randomly pick items from lists.

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#Creates a list containing all lowercase and uppercase alphabets.
#These will be used to randomly pick letter characters for the password.

numbers = ['0','1','2','3','4','5','6','7','8','9']
#Creates a list of number characters from 0 to 9.

symbols = ['!', '#', '$', '%', '(',')','*', '+']
#Creates a list of special symbol characters allowed in the password.

print("Welcome to Password Generator !")
#Displays a welcome message to the user.

n_letter = int(input("How many letters you want to your password ?\n"))
# Asks the user how many letters they want in the password.
# input() returns a string → int() converts it to a number (integer).

n_symbol = int(input("How many symbol you want to your password ?\n"))
#Asks the user how many symbols they want.

n_number = int(input("How many number you want to your password ?\n"))
#Asks the user how many numbers they want.

password = ""
#Creates an empty string where password characters will be added.

for i in range(1,n_letter+1):
    char1 = random.choice(letters)
    password = password + char1
# Loop runs n_letter times.
# Each time, random.choice(letters) picks a random letter from the letters list.
# Adds that letter to the password string.

for i in range(1,n_symbol+1):
    char2 = random.choice(symbols)
    password += char2
# Loop runs n_symbol times.
# Picks a random symbol using random.choice(symbols).
# password += char2 is the same as password = password + char2.

for i in range(1,n_number+1):
    char3 = random.choice(numbers)
    password += char3
# Loop runs n_number times.
# Each loop picks a random number character.
# Adds it to the password string.

print(password)
#Displays the generated password (letters + symbols + numbers).