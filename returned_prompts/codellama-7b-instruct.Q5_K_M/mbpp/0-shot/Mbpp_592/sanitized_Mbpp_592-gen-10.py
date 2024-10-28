def sum_Of_product(n):
    sum=0
    for i in range(n):
        sum=sum+(binomial(n,i)*binomial(n,n-i-1))
    return sum
def binomial(n,k):
    if k<0 or k>n:
        return 0
    if k==0 or k==n:
        return 1
    else:
        return binomial(n-1,k-1)+binomial(n-1,k)