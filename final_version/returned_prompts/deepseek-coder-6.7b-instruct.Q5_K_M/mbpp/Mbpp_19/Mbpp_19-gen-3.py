def test_duplicate(arr):
    return len(arr) != len(set(arr))

print(test_duplicate([1,2,3,4,5])) # False
"""
This function works by converting the array to a set, which removes any duplicate elements. It then checks if the lengths of the original array and the set are the same. If they are the same, there were no duplicates in the array and the function returns False. If the lengths are different, there were duplicates in the array and the function returns True.
"""
<jupyter_output>
False
<jupyter_text>
Question 2
<jupyter_code>
