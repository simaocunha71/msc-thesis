def similar_elements(l1, l2):
    return set(l1) & set(l2)

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))

#OUTPUT: {4, 5}

# The function works by converting the tuples to sets and finding the intersection. 
# The intersection of two sets is the set of elements that are common to both sets.
# The result is returned as a set.

# This function uses the & operator to find the intersection of the sets, which is a set of the elements that are common to both sets.
# The result is then returned as a set.

# The time complexity of this function is O(n+m), where n and m are the lengths of the two input lists.
# This is because in the worst case, we need to go through all the elements of both lists once.
# The space complexity is O(n+m), which is the space needed to store the two sets.

# The function assumes that the input lists do not contain any duplicate elements.
# If the input lists could contain duplicate elements, the function would need to convert the lists to sets before finding the intersection.
# This would change the time complexity to O(n+m) in the worst case, but the space complexity would still be O(n+m).
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:
<jupyter_code>
