def min_of_three(a,b,c):
    if a<b and a<c:
        return a
    elif b<c:
        return b
    else:
        return c

print(min_of_three(10,20,0)) #==0
assert min_of_three(10,20,0)==0
<jupyter_output>
0
<jupyter_text>
Problem 2
<jupyter_code>
