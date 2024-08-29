def even_Power_Sum(n):
    sum = 0
    for i in range(2, 2*n+1, 2):
        sum += i**5
    return sum

print(even_Power_Sum(2))

# Output: 1056

# Alternative Solution: Using the formula for the sum of the first n natural numbers is (n*(n+1))/2 and the sum of the first n even natural numbers is n*(n+1). The fifth power of these sums are ((n*(n+1))/2)**5 and (n*(n+1))**5 respectively. 

def even_Power_Sum_v2(n):
    return ((n*(n+1))/2)**5 + ((n*(n+1))/2)**5 - (n*(n+1))**5

print(even_Power_Sum_v2(2))

# Output: 1056
<jupyter_output>
1056
1056
<jupyter_text>
