
def tri(n):
    if n <= 1:
        return [1]
    if n % 2 == 0:
        return [1, n / 2] + tri(n - 1) + tri(n - 2) + tri(n + 1)
    else:
        return [1] + tri(n - 1) + tri(n - 2) + tri(n + 1)

def tri(n):
    if n <= 1:
        return [1]
    if n % 2 == 0:
        return [1, n / 2] + tri(n - 1) + tri(n - 2) + tri(n + 1)
    else:
        return [1] + tri(n - 1) + tri(n - 2) + tri(n + 1)

def tri(n):
    if n <= 1:
        return [1]
    if n % 2 == 0:
        return [1, n / 2] + tri(n - 1) + tri(n - 2) + tri(n + 1)
    else:
        return [1] + tri(n - 1) + tri(n - 2) + tri(n + 1)

def tri(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [1, n/2] + tri(n-1) + tri(n-2) + tri(n+1)
    else:
        return [1] + tri(n-1) + tri(n-2) + tri(n+1)

def tri(n):
    if n <= 1:
        return [1]
    return [1, n/2] + tri(n-1) + tri(n-2) + tri(n+1) if n % 2 == 0 else [1] + tri(n-1) + tri(n-2) + tri(n+1)

def tri(n):
    if n <= 1:
        return [1]
    return [1, n/2]