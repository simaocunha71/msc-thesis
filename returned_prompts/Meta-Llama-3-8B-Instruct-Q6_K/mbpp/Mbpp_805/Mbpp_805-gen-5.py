```
def max_sum_list(lists):
    max_sum = 0
    max_list = []
    for lst in lists:
        if sum(lst) > max_sum:
            max_sum = sum(lst)
            max_list = lst
    return max_list
```


In this problem, we need to find the list in a list of lists whose sum of elements is the highest. 

We initialize `max_sum` to 0 and `max_list` to an empty list. Then we iterate over each list in the list of lists. If the sum of the current list is greater than `max_sum`, we update `max_sum` and `max_list`. Finally, we return `max_list`.

The unit test `assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]` helps to clarify the problem by showing that the function should return the list with the highest sum of elements. It also helps to test the function by providing a specific input and expected output. 





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
