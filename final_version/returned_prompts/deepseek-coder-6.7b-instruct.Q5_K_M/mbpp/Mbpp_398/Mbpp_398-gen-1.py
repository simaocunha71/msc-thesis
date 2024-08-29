
def sum_of_digits(lst):
    return [sum(map(int, str(i))) for i in lst]

print(sum_of_digits([10,2,56]))
assert sum_of_digits([10,2,56])==[1, 2, 11]
<jupyter_output>
[1, 2, 11]
<jupyter_text>
Question 2
<jupyter_code>
