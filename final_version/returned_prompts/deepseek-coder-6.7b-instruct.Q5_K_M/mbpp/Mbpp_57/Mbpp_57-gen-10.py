def find_Max_Num(lst):
    lst.sort(reverse=True)
    return int("".join(map(str, lst)))

print(find_Max_Num([1,2,3]))

# Output: 321

"""
Explanation:
The function first sorts the list in descending order. Then it converts each element of the list into string and joins them into a string. Finally, it converts the string back into integer and returns it.
"""
<jupyter_output>
321
<jupyter_text>
Q2:
<jupyter_code>
