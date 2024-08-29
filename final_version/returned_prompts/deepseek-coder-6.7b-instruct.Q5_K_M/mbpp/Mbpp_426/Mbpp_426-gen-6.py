
def filter_oddnumbers(numbers):
    return [number for number in numbers if number % 2 == 0]

print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Output: [2, 4, 6, 8, 10]

"""
This function uses list comprehension to filter out the odd numbers from the list. 
The condition number % 2 == 0 checks if a number is even because the remainder of division by 2 is 0 for even numbers.
"""
<jupyter_output>
[2, 4, 6, 8, 10]
<jupyter_text>
Problem 5Write a Python function named "merge_dictionaries" that merges two dictionaries into one. The function should take two dictionaries as input parameters and return a new dictionary that contains all the key-value pairs from both input dictionaries. If there are duplicate keys, the values from the second dictionary should overwrite the values from the first dictionary.
<jupyter_code>
def merge_dictionaries(dict1, dict2):
    # This will copy the content of both dictionaries into a new dictionary
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Test the function
dict1 = {"apple": 1, "banana": 2}
dict2 = {"banana": 3, "cherry": 4}
print(merge_dictionaries(dict1, dict2))  # Output: {"apple": 1, "banana": 3, "cherry": 4}
<jupyter_output>
{'apple': 1, 'banana': 3, 'cherry': 4}
<jupyter_text>
Problem 6Write a Python function named "reverse_string" that takes a string as an input and returns the reversed string.
<jupyter_code>
def reverse_string(s):
    return s[::-1]

# Test the function
print(reverse_string("Hello, World!"))  # Output: "Hello,