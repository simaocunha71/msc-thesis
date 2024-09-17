
def catalan_number(n: int) -> int:
    return int( (1/(n+1)) * ( 2*n*choose(2*n,n) - choose(n,n) ) )

def choose(n: int, k: int) -> int:
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))


