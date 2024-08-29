def is_Monotonic(arr):
    return (all(arr[i] <= arr[i+1] for i in range(len(arr)-1))) or (all(arr[i] >= arr[i+1] for i in range(len(arr)-1)))

print(is_Monotonic([6, 5, 4, 4]))  # True
print(is_Monotonic([1, 2, 3, 4]))  # True
print(is_Monotonic([4, 3, 2, 1]))  # True
print(is_Monotonic([1, 2, 1, 4]))  # False
print(is_Monotonic([1, 3, 2, 4]))  # False


"""
This function takes an array as an argument. It returns True if the array is monotonic and False otherwise.
The function checks if all elements in the array are either in ascending order or in descending order. If they are, the function returns True. If not, it returns False.
"""
<jupyter_output>
True
True
True
False
False
<jupyter_text>
**Q3:**Write a Python function to find the intersection of two given arrays. The intersection means the common elements that these arrays have.**Test Cases:**assert intersection([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
<jupyter_code>
def intersection(arr1, arr2):
    return [value for value in arr1 if value in arr2]

print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]
<jupyter_output>
[3, 4]
<jupyter_text>
**Q4:**Given a string, write a Python function to reverse it.**Test Cases:**assert reverse_string("abcde") == "edcba"
<jupyter_code>
def reverse_string(s):
    return s[::-1]

print(reverse_