def similar_elements(list1, list2):
    return set(list1) & set(list2)

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))

# Expected output:
# {4, 5}

# This function works by converting each list to a set, and then using the & operator to find the intersection of the two sets, i.e., the common elements of the two lists. The result is returned as a set.
<jupyter_output>
{4, 5}
<jupyter_text>
2. Create a function which takes in a list of integers and returns the difference between the sum of the even and odd integers.
<jupyter_code>
