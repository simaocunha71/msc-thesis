"""
def divisor(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count

"""
def divisor(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count

# Testing the function
print(divisor(15)) # should print 4

# Testing the function with a different input
print(divisor(32)) # should print 8
"""
def divisor(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count

# Testing the function
assert divisor(15) == 4
# Testing the function with a different input
assert divisor(32) == 8

```
In the above function, we are using a for loop to iterate from 1 to the given number. For each iteration, we check if the given number is divisible by the current iteration number. If it is divisible, we increment the count by one. Finally, we return the count which gives us the number of divisors of the given number.

To test the function, we are using assertions to check if the function returns the correct result for the given inputs. If the function returns the correct result, the assertion passes and the function is correct.
```

---

Here are some more Python tips and tricks you might find helpful:

- How to check if a variable is an integer in Python
- How to convert a dictionary to a string in Python
- How to check if a list is empty in Python
- How to check if a string is a palindrome in Python
- How to check if a number is prime in Python
- How to get the first and last character of a string in Python
- How to get the index of the first occurrence of a substring in a string in Python
- How to get the index of the last occurrence of a substring in a string in Python
- How to find the common elements in two lists in Python
- How