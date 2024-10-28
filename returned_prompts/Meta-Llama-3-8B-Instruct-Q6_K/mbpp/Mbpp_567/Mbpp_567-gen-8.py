```
def issort_list(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```    
    The function issort_list checks whether a specified list is sorted or not. It uses the built-in function all() to check if all elements in the list are in order. The generator expression lst[i] <= lst[i+1] for i in range(len(lst)-1) checks each pair of adjacent elements in the list, ensuring they are in ascending order. If all pairs meet this condition, the function returns True, indicating the list is sorted. Otherwise, it returns False. 
    The unit test provided, assert issort_list([1,2,4,6,8,10,12,14,16,17])==True, ensures that the function correctly identifies a sorted list. 
```  



```
# test
print(issort_list([1,2,4,6,8,10,12,14,16,17]))  # Expected output: True
print(issort_list([1,2,3,4,5,6]))  # Expected output: True
print(issort_list([1,3,2,4,5,6]))  # Expected output: False
```  



```
Output:
True
True
False
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



```
```  



``