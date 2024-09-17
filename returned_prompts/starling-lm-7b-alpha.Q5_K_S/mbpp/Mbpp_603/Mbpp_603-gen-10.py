
def get_lucid(n):
    return [i for i in range(1,n+1) if all(i%j != 0 for j in range(1,int(i**0.5)+1))]


