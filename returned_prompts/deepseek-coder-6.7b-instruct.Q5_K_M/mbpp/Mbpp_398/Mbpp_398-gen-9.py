def sum_of_digits(lst):
    return [sum(int(i) for i in str(x)) for x in lst]


print(sum_of_digits([10,2,56]))
<jupyter_output>
[1, 4, 13]
<jupyter_text>
Q2:
<jupyter_code>
