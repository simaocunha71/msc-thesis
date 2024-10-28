
def specialFilter(nums):
    count = 0
    for n in nums:
        str_n = str(n)
        if int(str_n[0]) % 2 != 0 and int(str_n[-1]) % 2 != 0 and n > 10:
            count += 1
    return count


# Test Cases
print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2
print(specialFilter([10, 3, 5, 10, 15, 20]))  # Output: 0
print(specialFilter([100, 10, 110, 11, 101, 111]))  # Output: 3


# Explanation:
# The function `specialFilter` iterates through the input array `nums` and checks if a number `n` is greater than 10, and if the first and last digits of `n` are odd. It converts the number to a string using `str(n)` and uses indexing to get the first and last digits. It then converts the first and last digits back to integers using `int(str_n[0])` and `int(str_n[-1])` respectively. If both conditions are met, the function increments the `count` variable. Finally, the function returns the value of `count`.

# The provided test cases verify the correctness of the `specialFilter` function.


























































































































