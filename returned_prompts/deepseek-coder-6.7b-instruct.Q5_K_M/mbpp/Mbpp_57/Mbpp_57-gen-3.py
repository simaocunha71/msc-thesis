def find_Max_Num(lst):
    lst.sort(reverse=True)
    return int("".join(map(str, lst)))

print(find_Max_Num([1,2,3]))

# This function sorts the list in descending order and then joins the elements into a string, converting them to strings using the map() function.
# Finally, it converts the resultant string back to an integer and returns it.

"""
Output:
321
"""

# Explanation:
# The given list [1,2,3] is sorted in descending order to get [3,2,1].
# Then, the elements are joined into a string using the map() function to convert them into strings and then joined using the join() function.
# Finally, the string is converted back to an integer using the int() function. The result is 321, which is the largest number that can be formed with the given digits.
<jupyter_output>
321
<jupyter_text>
