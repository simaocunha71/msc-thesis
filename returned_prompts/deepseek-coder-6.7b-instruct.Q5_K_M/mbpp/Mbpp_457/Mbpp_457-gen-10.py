
def Find_Min(l):
    min_len = min(len(sublist) for sublist in l)
    for sublist in l:
        if len(sublist) == min_len:
            return sublist

print(Find_Min([[1],[1,2],[1,2,3]]))

"""
This function works by first finding the minimum length of any sublist in the input list.
It then iterates over the list and returns the sublist whose length matches the minimum length found earlier.
"""
<jupyter_output>
[1]
<jupyter_text>
Question 3
<jupyter_code>
