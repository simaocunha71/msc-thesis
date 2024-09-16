```
def pair_xor_Sum(my_list,n):
    sum=0
    for i in range(n):
        for j in range(i+1,n):
            sum+=my_list[i]^my_list[j]
    return sum
```