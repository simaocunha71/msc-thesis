
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and int(str(num)[0]) % 2 != 0 and int(str(num)[-1]) % 2 != 0:
            count += 1
    return count

# Testing the function
print(specialFilter([15, -73, 14, -15]))  # Expected output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Expected output: 2



# Here's how the function works:

# We initialize a counter variable called 'count' to 0.
# We then iterate over each number in the 'nums' array.
# For each number, we convert it to a string and check if the first and last digits are odd.
# If the number is greater than 10 and both its first and last digits are odd, we increment the 'count' variable.
# After iterating over all the numbers in the 'nums' array, we return the final value of the 'count' variable.


# The function takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and both the first and last digits of a number are odd (1, 3, 5, 7, 9).

# The function works by iterating over each number in the input array. For each number, it converts the number to a string and checks if the first and last digits are odd. If the number is greater than 10 and both its first and last digits are odd, it increments a counter variable. After iterating over all the numbers in the array, it returns the final value of the counter variable, which represents the number of elements in the array that satisfy the given conditions.

# The function returns the count of such elements in the array.






























































