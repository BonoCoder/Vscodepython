#data types
print(7+5)
print("7+5 eh 12, temos uma string aqui")
#then how you know what kind of data type they are? Use the command type
print(type("Hello"))

#---------------------------------------------------------------------------------------------

#VARIABLES
#ASSINGMENT is when you atribuite a value to a variable
#EXPRESSION is the combination of variables, numbers and symbols
number1 = 7
number2 = 5.5
sum = number1 + number2
print(sum)

#---------------------------------------------------------------------------------------------

#Data Conversions
print(2+2.5) #they are two types of variable, a integer and an float, this process is called implicit conversion.
print("A multiplicacao de " + str(number1) + " e " + str(number2) + " eh " + str(sum)) #Now we are using a explicit conversion, it can be str int and float

#---------------------------------------------------------------------------------------------

#FUNCTIONS
def dog(name, years):
    print("My dog name is " + name)
    print("He is " + years + " years old")
dog("bono", "14")    
#############################################
def area_triangle(base, height):
    return (base*height)/2
triangle1 = area_triangle(10, 5)     
print("area of defined triangle is " + str(triangle1)) 
#############################################
def seconds_transformation(sec):
    hour = sec // 3600
    minutes = (sec - hour * 3600) // 60 
    seconds = sec - hour * 3600 - minutes * 60
    return hour, minutes, seconds

secs = seconds_transformation(7000) #this way creates a array
hour, min, sec = seconds_transformation(7000) #this way creates three separate variables for each value
print(str(secs) + " <-- this is a array")
print(str(hour) + " hour " + str(min) + " minutes " + str(sec) + " seconds " + " <-- these are three variables") 
##############################################

#Comparison things
print(5 > 1) #bigger than
print(5 < 1) #smaller than
print(5 >= 1) #bigger or equal
print(5 <= 1) #smaller or equal
print(5 == 5) #equal
print(5 != 1) #not equal, inverts the comparison
 
#Comparison operators
#and = operator both must be true
#or = operator atleast once must be true
#not = Invert the comparison

#Conditional operators
def comparison_number(a,b):
    if a > b:
        print(str(a) + " is greater than " + str(b)) #Take care of identation of the condition
    elif a < b:
        print(str(a) + " is less than " + str(b))
    elif a == b:
        print(str(a) + " is equal to " + str(b))      
    else:
        print("The input is not a number")      
 

comparison_number(4,2) 
