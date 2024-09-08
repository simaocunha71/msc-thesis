def last(lst, x):
    return len(lst) - 1 - lst[::-1].index(x)

print(last([1,2,3,1],1)) # 3
print(last([1,2,3],1)) # 0

