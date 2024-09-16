```
def sum_Of_product(n):
    return sum([binomial_coefficient(n,i)*binomial_coefficient(n,n-i) for i in range(n)])

def binomial_coefficient(n,k):
    return (n-k+1)//(k+1)
```
