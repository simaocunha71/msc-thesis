
def count_samepair(a,b,c):
    return sum(x==y==z for x,y,z in zip(a,b,c))


