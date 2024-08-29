
def min_val(lst):
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val

print(min_val(['Python', 3, 2, 4, 5, 'version'])) # 2
<jupyter_output>
2
<jupyter_text>
Question 2
<jupyter_code>
