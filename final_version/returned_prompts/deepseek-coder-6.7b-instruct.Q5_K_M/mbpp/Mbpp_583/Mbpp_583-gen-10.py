def catalan_number(n):
    if n<=1:
        return 1
    catalan = [0 for _ in range(n+1)]
    catalan[0]=1
    catalan[1]=1
    for i in range(2,n+1):
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j]*catalan[i-j-1]
    return catalan[n]

print(catalan_number(10))

# Output: 16796
<jupyter_output>
16796
<jupyter_text>
Problem 3
<jupyter_code>
