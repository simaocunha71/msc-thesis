def pair_wise(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]

print(pair_wise([1,1,2,3,3,4,4,5]))

# Q2
