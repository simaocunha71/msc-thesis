def Find_Min_Length(lst):
    return min(len(sub_lst) for sub_lst in lst)

print(Find_Min_Length([[1],[1,2]]))
assert Find_Min_Length([[1],[1,2]]) == 1
<jupyter_output>
1
<jupyter_text>
Question 2
<jupyter_code>
