def sum_average(n: int) -> tuple:
    return (n*(n+1)//2, n//2 if n%2==0 else n//2+1)