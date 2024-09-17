def minimum(a, b):
    if a < b:
        return a
    else:
        return b
assert minimum(1,2) == 1
print(minimum(1,2)) # Output: 1

#Explanation: 
#The function `minimum(a, b)` takes two numbers as arguments and returns the smallest one.
#It compares the two numbers and returns the smaller one.
#The unit test `assert minimum(1,2) == 1` ensures that the function works correctly.
#The function is then called with the arguments 1 and 2, and the output is printed. 

#Alternate Solution:
def minimum(a, b):
    return min(a, b)
assert minimum(1,2) == 1
print(minimum(1,2)) # Output: 1

#Explanation: 
#The function `minimum(a, b)` takes two numbers as arguments and returns the smallest one using the built-in `min()` function.
#The unit test `assert minimum(1,2) == 1` ensures that the function works correctly.
#The function is then called with the arguments 1 and 2, and the output is printed. 