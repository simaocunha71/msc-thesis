
def catalan_number(n):
    if n<=1:
        return 1
    catalan = [0 for i in range(n+1)]
    catalan[0]=1
    catalan[1]=1
    for i in range(2,n+1):
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j]*catalan[i-j-1]
    return catalan[n]


print(catalan_number(10))
<jupyter_output>
16796
<jupyter_text>
Question 3:Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.An input string is valid if:Open brackets must be closed by the same type of brackets.Open brackets must be closed in the correct order.Note that an empty string is also considered valid.
<jupyter_code>
