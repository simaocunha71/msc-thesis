
def f(n):
    # Create an empty list to store the results
    result = []

    # Loop through each index from 1 to n
    for i in range(1, n+1):
        # If the index is even, calculate the factorial and append it to the result
        if i % 2 == 0:
            result.append(factorial(i))
        # Otherwise, calculate the sum and append it to the result
        else:
            result.append(sum_numbers(i))

    return result

# Helper function to calculate the factorial of a number
def factorial(n):
    # Base case: if the number is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: calculate the factorial of n by multiplying n with the factorial of n-1
    else:
        return n * factorial(n-1)

# Helper function to calculate the sum of numbers from 1 to n
def sum_numbers(n):
    # Base case: if the number is 0 or 1, return the number itself
    if n == 0 or n == 1:
        return n
    # Recursive case: calculate the sum of numbers from 1 to n by adding n to the sum of numbers from 1 to n-1
    else:
        return n + sum_numbers(n-1)

# Test the function
print(f(5))  # Output: [1, 2, 6, 24, 15]









































































































































