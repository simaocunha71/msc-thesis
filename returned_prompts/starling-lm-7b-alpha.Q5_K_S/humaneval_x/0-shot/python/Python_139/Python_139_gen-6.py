
def special_factorial(n):
    if(n <= 1):
        return 1
    else:
        return n * special_factorial(n-1)


# Test cases
print(special_factorial(4))  # 288
print(special_factorial(5))  # 720
print(special_factorial(0))  # 1


# Recursive function to calculate factorial
def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n-1)

# Recursive function to call itself multiple times
# This function will call itself multiple times till the base case is reached
# The base case is n <= 1 which means the factorial of 0 or 1 is 1
# In each recursive call we reduce the value of n by 1 and return n*factorial(n-1)
```