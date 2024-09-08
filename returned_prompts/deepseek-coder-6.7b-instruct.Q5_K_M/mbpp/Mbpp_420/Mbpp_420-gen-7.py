def cube_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*2
    return sum**3

print(cube_Sum(2))

# OR

def cube_Sum(n):
    sum = 0
    for i in range(2, 2*n+1, 2):
        sum += i
    return sum**3

print(cube_Sum(2))

# OR

def cube_Sum(n):
    return ((n**2)*(2*n+1))**2

print(cube_Sum(2))

# OR

def cube_Sum(n):
    return ((n*(n+1)*(2*n+1))//2)**2

print(cube_Sum(2))

# OR

def cube_Sum(n):
    return ((2*n+1)**3)//3

print(cube_Sum(2))

# OR

def cube_Sum(n):
    return (8*n**3 + 3*n**2 + 3*n)//3

print(cube_Sum(2))

# OR

def cube_Sum(n):
    return (n*(n+1)*(2*n+1)//2)**2

print(cube_Sum(2))
<jupyter_output>
72
72
72
72
72
72
72
72
<jupyter_text>
