def sum_to_n(n: int):
    if n < 0:
        return "Error: Input must be a positive integer."
    elif n == 0:
        return 0
    else:
        return sum(range(1, n+1))
    # This function returns the sum of numbers from 1 to n. It uses the built-in sum function and range function in Python.
    # The range function generates a sequence of numbers from 1 to n (inclusive), and the sum function adds them up.
    # The function also handles edge cases where n is less than 0 or equal to 0.

    # Example usage:
    print(sum_to_n(30))  # Output: 465
    print(sum_to_n(100))  # Output: 5050
    print(sum_to_n(5))  # Output: 15
    print(sum_to_n(10))  # Output: 55
    print(sum_to_n(1))  # Output: 1
    # This function can be used to calculate the sum of numbers from 1 to any positive integer.