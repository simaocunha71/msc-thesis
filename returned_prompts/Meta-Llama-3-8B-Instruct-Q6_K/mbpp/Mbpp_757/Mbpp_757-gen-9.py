```
def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j][::-1]:
                count += 1
            elif lst[j] == lst[i][::-1]:
                count += 1
    return count
```
The function `count_reverse_pairs` takes a list of strings as input and returns the count of pairs of reverse strings. It iterates over the list and checks each string with every other string in the list. If a string is equal to the reverse of another string, it increments the count by 1. It also checks for the reverse condition in the other direction to count both types of pairs. Finally, it returns the total count. 

The unit test `assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2` ensures that the function works correctly by checking that the count of reverse pairs in the given list is 2. 





```
python
```


```
def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j][::-1]:
                count += 1
            elif lst[j] == lst[i][::-1]:
                count += 1
    return count
```
```

python
```


```
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
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