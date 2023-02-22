#-------------------------------------------------------------
text1 = "its a text"
text2 = 'ts another text'

# we can also do operations with strings
text = "Bono "
print(text * 3)

# Len is used to return the length of the string
print(len(text))

# some examples of indexing if a string is
print(text[0])
print(text[-2])
print(text[2:4])

#Note, strings do not support item assignment, they are immutable

#we can create another one using the old one.
phrase = text[:2] + "naldo"
print(phrase)

#method to find a character in a string
print(phrase.index("o"))  #return the first occurrence of the character.
print("dog" in phrase)  #returns true if the character is present in the string, and false otherwise.

# Real application------------------------------------------------------------------------------
def change_domain(email, new_domain, old_domain):
    if old_domain in email:
        index = email.index(old_domain)
        email = email[:index] + new_domain
        print(email)
    return

change_domain("adampaiva@lactec.org.br", "lactec.com.br", "lactec.org.br")

# Another strings methods
print(phrase.upper()) #transform the string to upper case
print(phrase.lower()) #transform the string to lower case
print(phrase.capitalize())
print(phrase.title()) 
print(phrase.strip()) #remove white spaces from both sides of the string
print(phrase.lstrip()) #remove white spaces from the left side of the string
print(phrase.rstrip()) #remove white spaces from the right side of the string
print(phrase.count("o")) #count the number of occurrences of the character in the string
print(phrase.find("o")) #find the first occurrence of the character in the string
print(phrase.rfind("o")) #find the last occurrence of the character in the string
print(phrase.replace("o", "a", 4)) #replace the character in the string untill the fourth occurrence
print(phrase.endswith("o")) #check if the string ends with the character
print(phrase.startswith("o")) #check if the string starts with the character
print(phrase.isnumeric()) #check if the string is numeric
print(phrase.join(["viva ", " ola ", " opa ", " beijo "])) #join a list of strings
print("hello beautiful world".split(" ")) #split the string by white spaces

# formatting strings

print("My dogs name is {}, and his age is {} years old".format(phrase, 14))
price = 150.5891
print("My dogs food cust {:.2f} in the store and in delivery cust {:.2f} BRL".format(price, price * 1.1))
 # using the parameters :.2f means to format the number with 2 decimal places 
 # and allign it to the right side of the string

print('{:>3.4s}'.format(phrase))
print('{:<3.4s}'.format(phrase))
print('{:^3.4s}'.format(phrase))
