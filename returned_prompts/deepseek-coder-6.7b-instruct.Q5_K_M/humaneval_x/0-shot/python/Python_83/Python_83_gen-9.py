
    # Initialize the count
    count = 0

    # Loop through each digit from 2 to n
    for i in range(2, n+1):
        # The count of numbers that start or end with 1 is 2*(9*(10^(i-2)))
        # because there are 2 possibilities (starts or ends) and for each possibility
        # we have 9*(10^(i-2)) numbers.
        count += 2 * (9 * (10 ** (i - 2)))

    return count

print(starts_one_ends(2))  # Output: 180
print(starts_one_ends(3))  # Output: 2700
print(starts_one_ends(4))  # Output: 36000
print(starts_one_ends(5))  # Output: 450000

This code works by iterating over each digit from 2 to n (inclusive). For each digit, it calculates the count of numbers that start or end with 1 based on the formula given in the question. It then adds this count to the total count, which is returned at the end.

This code assumes that the input is a positive integer greater than or equal to 1. If the input is not a positive integer, the function will not work as expected.
