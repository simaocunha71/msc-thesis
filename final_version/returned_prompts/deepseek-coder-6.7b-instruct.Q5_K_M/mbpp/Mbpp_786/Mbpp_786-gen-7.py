def right_insertion(arr, value):
    for i in range(len(arr)):
        if value < arr[i]:
            return i
    return len(arr)

print(right_insertion([1,2,4,5],6))

"""
The function works by iterating through the array and checking if the value is less than each element. 
If it is, it returns the index of that element. 
If the value is not less than any element, it returns the length of the array. 
This means that the value will be inserted at the end of the array.
"""
<jupyter_output>
4
<jupyter_text>
Question 3:Write a Python function that takes a list of numbers and returns the sum of the list. If the list is empty, it should return 0.
<jupyter_code>
def sum_list(nums):
    return sum(nums)

print(sum_list([1,2,3,4,5]))
print(sum_list([]))
<jupyter_output>
15
0
<jupyter_text>
Question 4:Write a Python function that takes a list of numbers and returns the maximum and minimum values from that list. If the list is empty, it should return None for both values.
<jupyter_code>
def max_min(nums):
    if not nums:
        return None, None
    return max(nums), min(nums)

print(max_min([1,2,3,4,5]))
print(max_min([]))
<jupyter_output>
(5, 1)
(None, None)
<jupyter_text>
Question 5:Write a Python function that takes a list of strings and returns a new list with all strings that start with the letter 'a' or 'A'.
<jupyter_code>
def filter_strings(strings):
    return [s for s in strings if s[0].lower() == 'a']

print(filter_strings(["apple", "banana", "Avocado", "cherry", "grape"]))