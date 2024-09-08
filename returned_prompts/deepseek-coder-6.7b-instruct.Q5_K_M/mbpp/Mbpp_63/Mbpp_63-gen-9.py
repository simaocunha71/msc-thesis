def max_difference(lst):
    return max(max(x)-min(x) for x in lst)

print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))
<jupyter_output>
7
<jupyter_text>
Q2:
<jupyter_code>
