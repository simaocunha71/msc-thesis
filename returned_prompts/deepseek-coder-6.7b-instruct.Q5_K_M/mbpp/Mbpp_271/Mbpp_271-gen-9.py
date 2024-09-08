def even_Power_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += 2*i**5
    return sum

assert even_Power_Sum(2) == 1056

# OR

def even_Power_Sum(n):
    return sum(2*i**5 for i in range(1, n+1))

assert even_Power_Sum(2) == 1056

# OR

def even_Power_Sum(n):
    return sum(2*(2*i)**5 for i in range(1, n+1))

assert even_Power_Sum(2) == 1056

# OR

def even_Power_Sum(n):
    return sum(i**5 for i in range(2, 2*n+1, 2))*32

assert even_Power_Sum(2) == 1056

# OR

def even_Power_Sum(n):
    return sum(map(lambda i: i**5 * 2, range(1, n+1)))

assert even_Power_Sum(2) == 1056

# OR

def even_Power_Sum(n):
    return sum(map(lambda i: (i*2)**5, range(1, n+1)))

assert even_Power_Sum(2) == 1056
<jupyter_output>
<empty_output>
<jupyter_text>
