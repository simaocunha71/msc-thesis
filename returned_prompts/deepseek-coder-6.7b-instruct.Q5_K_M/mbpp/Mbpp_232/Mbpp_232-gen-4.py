def larg_nnum(nums, n):
    return sorted(nums, reverse=True)[:n]

print(set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)))
<jupyter_output>
{90, 100}
<jupyter_text>
Q2:
<jupyter_code>
