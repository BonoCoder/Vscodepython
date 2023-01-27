# In this week we gonna learn about loops!

# While loops
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

#----------------------------------------------------------------

# For loops

