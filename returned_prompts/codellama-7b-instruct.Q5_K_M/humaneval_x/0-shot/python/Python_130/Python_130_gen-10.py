
def tri(n):
    if n <= 0:
        return []
    if n == 1:
        return [3]
    if n % 2 == 0:
        return [3] + tri(n - 1) + tri(n - 2) + tri(n + 1)
    else:
        return [3] + tri(n - 1) + tri(n - 2) + tri(n + 1)

# 3. 
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# 4. 
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

# 5. 
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# 6. 
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 7. 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 8. 
def fibonacci(n):
    if n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 9. 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 10.