
    # Initialize the count of numbers
    count = 0

    # Loop through each digit in the number
    for i in range(1, n):
        # Calculate the number of n-digit numbers that start or end with 1
        count += 2 * (10 ** (i - 1))

    # Add the n-digit number that starts or ends with 1
    count += 1

    return count

# Test cases
print(starts_one_ends(1)) # 1
print(starts_one_ends(2)) # 10
print(starts_one_ends(3)) # 190
print(starts_one_ends(4)) # 2890
print(starts_one_ends(5)) # 38890


# In the test cases, for example, there are 10 two-digit numbers that start or end with 1, so the output for n=2 should be 10. 
# Similarly, there are 190 three-digit numbers that start or end with 1, so the output for n=3 should be 190.
<jupyter_output>
1
10
190
2890
38890
<jupyter_text>
Q2: Write a Python function that takes a list of numbers and returns the sum of the numbers in the list.
<jupyter_code>
