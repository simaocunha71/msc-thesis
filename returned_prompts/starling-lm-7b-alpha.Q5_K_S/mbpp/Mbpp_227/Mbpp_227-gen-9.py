def min_of_three(a,b,c):
    if (a<b and a<c):
        return a
    elif(b<c):
        return b
    else:
        return c

# Testing
assert min_of_three(10,20,0)==0

"""
Write a function to check if a number is even or odd.
assert is_even(3)==False
"""
def is_even(n):
    if n%2==0:
        return True
    else:
        return False

# Testing
assert is_even(3)==False

"""
Write a function to check if a string is palindrome. A palindrome is a string that reads the same forwards and backwards.
assert is_palindrome("racecar")==True
"""
def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True

# Testing
assert is_palindrome("racecar")==True

"""
Write a function to return the first k Fibonacci numbers. A Fibonacci number is a number in the Fibonacci sequence. The first two numbers in the Fibonacci sequence are 0 and 1. Every subsequent number is the sum of the previous two.
assert fibonacci(5)==[0,1,1,2,3]
"""
def fibonacci(k):
    fib_list = [0,1]
    while len(fib_list) < k:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:k]

# Testing
assert fibonacci(5)==[0,1,1,2,3]

"""
Write a function to return the sum of all divisors of a number. The divisors of a number are all the positive integers less than or equal to it that divide the number without a remainder. For example, the divisors of 12 are 1, 2, 3, 4, 6, and 12