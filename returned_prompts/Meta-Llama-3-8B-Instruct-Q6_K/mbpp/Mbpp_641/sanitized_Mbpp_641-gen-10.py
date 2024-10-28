def is_nonagonal(n):
    if n < 1:
        return None
    return int((n*(8*n-1))//2)  # Nonagonal numbers formula: (n*(8n-1))/2