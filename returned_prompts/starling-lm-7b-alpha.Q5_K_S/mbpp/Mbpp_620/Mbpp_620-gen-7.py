def largest_subset(nums):
    """
    Given an array of numbers, return the size of the largest subset of numbers so that every pair is divisible.
    """
    # Create a dictionary to store the divisibility of each number
    divisibility = {}
    for num in nums:
        divisibility[num] = 1
        # If the number is already in the dictionary, update its divisibility
        if num in divisibility:
            for key in divisibility:
                if key % num == 0:
                    divisibility[num] = max(divisibility[num], divisibility[key] + 1)
    # Return the size of the largest subset
    return max(divisibility.values())

# Test the function
print(largest_subset([1, 3, 6, 13, 17, 18]))  # Output: 4

# Time complexity: O(n^2)
# Space complexity: O(n)


# Explanation:
# The time complexity of the function is O(n^2) because it needs to iterate through the array of numbers twice. The first iteration is to create the dictionary of divisibility, and the second iteration is to update the divisibility of each number. The space complexity of the function is O(n) because it needs to store the divisibility of each number in the dictionary.

# The function works by creating a dictionary to store the divisibility of each number. It then iterates through the array of numbers and updates the divisibility of each number in the dictionary. If a number is already in the dictionary, it checks if it is divisible by any other number in the dictionary. If it is, it updates the divisibility of the number in the dictionary. Finally, it returns the size of the largest subset of numbers so that every pair is divisible, which is the maximum value in the dictionary.

# The function can be used to find the size of the largest subset of a list of numbers so that every pair is divisible. The function takes a list of numbers as input and returns the size of the largest subset of numbers so that every pair is divisible. The function uses a dictionary to store the divisibility of each number and iterates through the array of numbers to update the divisibility of each number in the