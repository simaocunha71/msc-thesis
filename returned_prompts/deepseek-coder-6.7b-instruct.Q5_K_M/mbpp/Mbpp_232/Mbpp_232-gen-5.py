def larg_nnum(l,n):
    l.sort(reverse=True)
    return l[:n]

print(set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)))
<jupyter_output>
{90, 100}
<jupyter_text>
Question 2
<jupyter_code>
