
def larg_nnum(numbers, n):
    numbers.sort(reverse=True)
    return numbers[:n]

print(set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)))
<jupyter_output>
{90, 100}
<jupyter_text>
Problem 5
<jupyter_code>
