def similar_elements(list1, list2):
    return set(list1) & set(list2)

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))

#Output: {4, 5}

#Note: 
#The function uses the '&' operator for set intersection.
#The function converts the lists to sets, which removes duplicates from each list, and then finds the intersection of the sets.
#The result is a set of elements that appear in both lists.
#The function returns this set as the result.
<jupyter_output>
{4, 5}
<jupyter_text>
Question 2
<jupyter_code>
