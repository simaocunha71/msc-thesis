```
def sum_Of_Subarray_Prod(my_list):
    result = 0
    for i in range(len(my_list)):
        for j in range(i,len(my_list)):
            result+=prod(my_list[i:j+1])
    return result

def prod(my_list):
    result = 1
    for i in my_list:
        result*=i
    return result
```
