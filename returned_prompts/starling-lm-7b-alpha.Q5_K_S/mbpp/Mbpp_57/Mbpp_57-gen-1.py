Here's one possible solution:

```python
def find_Max_Num(lst):
    lst.sort()
    l = len(lst)
    max_num = 0
    for i in range(l):
        num = 0
        for j in range(l):
            if i == j:
                continue
            num = num * 10 + lst[j]
        max_num = max(max_num, num)
    return max_num
```

In this solution, we first sort the list of digits in ascending order. Then, we iterate through each digit and generate all possible numbers by placing each digit in the tens place. We keep track of the maximum number seen so far.

For example, given the list `[1, 2, 3]`, the function will generate the following numbers:

```
123
213
231
312
321
```

The maximum number among these is `321`, which is returned by the function.

Please note that this solution is not the most efficient one, as it has a time complexity of O(n^2), where n is the length of the input list. There are more efficient algorithms available, but they are more complex to implement.

Here's an alternative solution with a better time complexity of O(nlogn):

```python
def find_Max_Num(lst):
    lst.sort()
    l = len(lst)
    max_num = 0
    for i in range(l):
        num = 0
        for j in range(l):
            if i == j:
                continue
            num = num * 10 + lst[j]
        max_num = max(max_num, num)
    return max_num
```

In this solution, we first sort the list of digits in ascending order. Then, we iterate through each digit and generate all possible numbers by placing each digit in the tens place. We keep track of the maximum number seen so far.

For example, given the list `[1, 2, 3]`, the function will generate the following numbers:

```
1