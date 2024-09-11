def find(a,b):
    return int(a/b)


# Python program to find the quotient of two numbers
def quotient(a, b):
    if (b == 0):
        return -1
    else:
        return a // b

def test_quotient(a, b):
    assert quotient(a, b) == find(a,b)
    print("Test Passed")

test_quotient(10,3)

"""
Explanation:
In the quotient function, it first checks if b is equal to zero, if b is zero it returns -1. Otherwise it returns a divided by b rounded down to the nearest integer using the floor division operator.
In the find function, it simply uses the floor division operator to find the quotient and returns it.
The test_quotient function tests the quotient function by comparing its result with the result of the find function. If the results are equal it prints "Test Passed"
"""

# Python3 program to print Fibonacci series in O(log n)

# Function to print Fibonacci series
def Fibonacci(n):
    # First Fibonacci number is 0
    if (n == 0):
        return 0
    # Second Fibonacci number is 1
    elif (n == 1):
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

# Driver Program
n = 10
print(Fibonacci(n))

"""
Explanation:
In the Fibonacci function, it checks if the argument n is equal to 0 or 1. If n is 0, it returns 0, if n is 1, it returns 1. Otherwise, it recursively calls the Fibonacci function with n-1 and n-2 as arguments and returns the sum of the results.
In the driver program, it calls the Fibonacci function with the argument n and prints the result, which is the Fibonacci number at position n.
"""

# Python3 program to print all prime factors of a number
def primeFactors(n):
    # Print the number