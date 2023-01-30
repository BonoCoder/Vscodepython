# In this week we gonna learn about loops!

# ________________________________While loops
# we need a starter variable to work as control
# A expression to compare if the look will be started or not
# Then a expression to increase or decrease our variable
# is about TRUE or FALSE


#----------------------- Exemple --------------------------------
def attempt(n):
    x = 1 #control variable started
    while (x <= n): #condition of the while loop
        print("we are in the attempt: " + str(x)) # intern expression
        x += 1 #expression to increment x value
    print("Done")  

attempt(10)

#----------------------- Exemple --------------------------------
def sum_divisors(n):
  x = 1
  sum = 0
  while (x <= n):
    if (n % x) == 0:
        sum = sum + x    
    x += 1

  # Return the sum of all divisors of n, not including n
  return (sum - n)

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

#------------------------------------For loops------

# For loops is used when we have a sequence of elements
for x in range(5): # Loop
    print(x)    #The variable x starts from 0 and ends in 4, because the loop never includes the last element
    #also the fuctions range have 3 parameters (initial value, final value, increment)
    #range (1,11,2) It will go from 1 to 10 by step 2.


friends = ['marcos', 'fernando', 'diego', 'joao']  #This is a array of friends
for friend in friends:
  print(friend + " is his name")

print()

#----------------------------------------------------------------
# Nested Loops are about loops inside other loop
# Exemple: Each team must play once with each others, divided by away and home.

Brazil_teams = ['Vasco', 'Sao Paulo', 'Curitiba', 'Gremio']
print("away_teams " + " home_teams")
for away_teams in Brazil_teams:
  for home_teams in Brazil_teams:
    if away_teams != home_teams:
      print(away_teams + " vs " + home_teams)

print()




#---------------------------- Recursion ------------------

def factorial(n):
  if n < 2:
    return 1
  return n * factorial(n-1)

print(factorial(5))