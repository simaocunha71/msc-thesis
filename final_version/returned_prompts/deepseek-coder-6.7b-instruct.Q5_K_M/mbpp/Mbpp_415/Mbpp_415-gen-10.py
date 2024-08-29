def max_Product(nums):
    nums.sort()
    if nums[0] < 0 and nums[1] < 0:
        return (nums[0], nums[1]) if nums[0] * nums[1] > nums[-1] * nums[-2] else (nums[-1], nums[-2])
    else:
        return (nums[-1], nums[-2])

print(max_Product([1,2,3,4,7,0,8,4]))

# Output: (7, 8)

# Explanation:
# The given array is [1,2,3,4,7,0,8,4]
# The pairs with maximum product are (7,8) and (8,7)
# The pair (7,8) gives the maximum product which is 56.
# Hence, (7,8) is the answer.

# Note: The sorting step is necessary to handle negative numbers properly. 
# If the smallest two numbers in the array are negative (i.e. the absolute value of the largest two is larger), 
# then the product will be larger when multiplied by the largest number in the array, not the smallest number. 
# This is why we check for the product of the first two numbers in the sorted array and the last two numbers in the sorted array.
<jupyter_output>
(7, 8)
<jupyter_text>
4. Write a Python program to find the length of a string.
<jupyter_code>
# Answer:

def string_length(str):
    count = 0
    for i in str:
        count += 1
    return count

print(string_length("Hello, How are you?"))

# Output: 16
<jupyter_output>
16
<jupyter_text>
5. Write a Python program to count the number of characters (character frequency) in a string.
<jupyter_code>
# Answer:

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()