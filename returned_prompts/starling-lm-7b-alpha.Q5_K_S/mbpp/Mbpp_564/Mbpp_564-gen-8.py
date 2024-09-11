"""
def count_Pairs(l,n):
    count=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]!=l[j]:
                count+=1
    return count


"""

def count_Pairs(l,n):
    return len(set(l))*(len(set(l))-1)

assert count_Pairs([1,2,1],3) == 2
print("All tests passed")

# This code is contributed by Ankur Singh(Ankur1991)


