
def count_samepair(a,b,c):
    return sum(i==j==k for i,j,k in zip(a,b,c))


