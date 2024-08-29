
def larg_nnum(lst, n):
    return sorted(lst, reverse=True)[:n]

print(set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)))

# Alternate solution

def n_largest_nums(lst, n):
    lst.sort()
    return lst[-n:]

print(set(n_largest_nums([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)))

# Output: {100, 90}

"""
Explanation:
The function `larg_nnum` sorts the list in descending order and then returns the first n elements. The function `n_largest_nums` sorts the list in ascending order and then returns the last n elements. Both functions will return the same output.
"""
<jupyter_output>
{100, 90}
{100, 90}
<jupyter_text>
Question 2
<jupyter_code>
