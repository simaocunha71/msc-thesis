
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and int(str(num)[0]) % 2 != 0 and int(str(num)[-1]) % 2 != 0:
            count += 1
    return count

# testing
print(specialFilter([15, -73, 14, -15]))   # 1
print(specialFilter([33, -2, -3, 45, 21, 109]))   # 2





# Solution

def specialFilter(nums):
    # Initialize the count to 0
    count = 0
    # Iterate through the list of numbers
    for num in nums:
        # Check if the number is greater than 10
        if num > 10:
            # Convert the number to a string to get the first and last digits
            str_num = str(num)
            # Check if the first and last digits are odd
            if int(str_num[0]) % 2 != 0 and int(str_num[-1]) % 2 != 0:
                # If both conditions are true, increment the count by 1
                count += 1
    # Return the count
    return count

# Test cases
print(specialFilter([15, -73, 14, -15]))   # Expected output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))   # Expected output: 2





# Solution

def specialFilter(nums):
    # Initialize the count to 0
    count = 0
    # Iterate through the list of numbers
    for num in nums:
        # Check if the number is greater than 10
        if num > 10:
            # Convert the number to a string to get the first and last digits
            str_num = str(num)
            # Check if the first and last digits are odd
            if int(str_num[0]) % 2 != 0 and int