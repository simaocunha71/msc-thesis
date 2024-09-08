def test_duplicate(arr):
    return len(arr) != len(set(arr))

print(test_duplicate([1,2,3,4,5]))

# Alternatively, you can use the following code:

def test_duplicate(arr):
    num_dict = {}
    for num in arr:
        if num in num_dict:
            return True
        num_dict[num] = True
    return False

print(test_duplicate([1,2,3,4,5]))

# Both codes work and are correct as they use a set or dictionary to store the elements of the array. 
# If the element is already in the set/dictionary, it means the element is a duplicate, so the function returns True. 
# If the element is not in the set/dictionary, it is added to the set/dictionary and the function returns False.
<jupyter_output>
False
False
<jupyter_text>
Question 2
<jupyter_code>
