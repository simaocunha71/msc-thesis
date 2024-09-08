
def Extract(lst):
    result = [i[0] for i in lst if isinstance(i, list)]
    return result

print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))
<jupyter_output>
[1, 3, 6]
<jupyter_text>
Exercise 3:
<jupyter_code>
