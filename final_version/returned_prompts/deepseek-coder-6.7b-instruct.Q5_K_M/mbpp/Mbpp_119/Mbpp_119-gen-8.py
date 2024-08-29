def search(arr):
    for i in range(0, len(arr), 2):
        if i == len(arr)-1 or arr[i] != arr[i+1]:
            return arr[i]
    return None

print(search([1,1,2,2,3])) # 3

"""
Explanation:
The function works by iterating over the array in steps of 2 (i.e. it looks at every second element). If it ever encounters a pair of elements that are different (or if it reaches the end of the array), it returns the first element of that pair. This is the element that appears only once in the array. If no such element is found, it returns None.
"""
<jupyter_output>
3
<jupyter_text>
Problem 2
<jupyter_code>
