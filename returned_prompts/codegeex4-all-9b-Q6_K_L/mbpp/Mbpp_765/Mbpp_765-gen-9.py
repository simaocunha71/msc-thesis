def is_polite(n):
    if n==1:
        return 1
    else:
        return (n-1) + is_polite(n-1) + is_polite(n-2)

