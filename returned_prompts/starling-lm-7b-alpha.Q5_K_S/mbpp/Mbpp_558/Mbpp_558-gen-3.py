def digit_distance_nums(num1, num2):
    # Convert the numbers to strings to easily access the digits
    str_num1 = str(num1)
    str_num2 = str(num2)

    # Initialize the result to 0
    result = 0

    # Compare the digits of the numbers and calculate the per-digit difference
    for digit1, digit2 in zip(str_num1, str_num2):
        result += abs(int(digit1) - int(digit2))

    return result

# Test the function
assert digit_distance_nums(1, 2) == 1
print("All tests passed.")



# Time Complexity: O(n), where n is the maximum of the length of num1 and num2
# Space Complexity: O(1), as we are using a fixed amount of space to store the result

# The function takes in two integers, num1 and num2, and converts them to strings to easily access the digits. It initializes the result to 0 and then iterates through the digits of the numbers using the zip function. For each digit, it calculates the absolute difference between the corresponding digits of num1 and num2 and adds it to the result. Finally, it returns the result.

# The time complexity of the function is O(n), where n is the maximum of the length of num1 and num2, as we iterate through each digit of the numbers. The space complexity is O(1), as we are using a fixed amount of space to store the result and the input parameters.































"""
def digit_distance_nums(num1, num2):
    # Convert the numbers to strings to easily access the digits
    str_num1 = str(num1)
    str_num2 = str(num2)

    # Initialize the result to 0
    result = 0

    # Compare the digits of the numbers and calculate the per-digit difference
    for digit1, digit2 in zip(str_num1, str_num2):
