# The number we will perform the Collatz operation on
n = int(input("Enter a positive integer: "))

# keep looping until we reach 1.
# assuming the collatz conjecture is true 
while n != 1:
    # print current n value 
     print(n)
     # see if n is even  
     if n % 2 == 0:
         # if n is even divide by two 
        n = n / 2
     else:
         # if n is odd, multiply by three and add one
        n = (3 * n) + 1

# print n value       
print(n)
