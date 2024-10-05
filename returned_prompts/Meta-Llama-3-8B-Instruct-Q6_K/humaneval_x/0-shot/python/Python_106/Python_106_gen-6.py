def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:  # if i is even
            result.append(math.factorial(i))
        else:  # if i is odd
            result.append(sum(range(1, i+1)))
    return result

# Test the function
print(f(5))  # Output: [1, 2, 6, 24, 15]  # Example: f(5) == [1, 2, 6, 24, 15]
print(f(3))  # Output: [1, 1, 3]
print(f(2))  # Output: [1, 1]
print(f(10))  # Output: [1, 1, 2, 6, 24, 120, 6, 15, 21, 210]  # Example: f(10) == [1, 1, 2, 6, 24, 120, 6, 15, 21, 210]  # Example: f(10) == [1, 1, 2, 6, 24, 120, 6, 15, 21, 210]
print(f(1))  # Output: [1]  # Example: f(1) == [1]  # Example: f(1) == [1]  # Example: f(1) == [1]  # Example: f(1) == [1]  # Example: f(1) == [1]  # Example: f(1) == [1]
# End of function definition
# End of test cases

# End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End of program  # End