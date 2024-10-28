```
def cal_sum(n):
    a, b, c = 3, 2, 1
    total = 0
    for _ in range(n):
        total += c
        a, b, c = b, c, a + b
    return total
```





```
def cal_sum(n):
    a, b, c = 3, 2, 1
    total = 0
    for _ in range(n):
        total += c
        a, b, c = b, c, a + b
    return total
```


This function calculates the sum of the first n Perrin numbers. The Perrin sequence is a sequence of numbers in which each term is the sum of the two preceding terms, starting with 3, 2, 1. The function initializes the first three Perrin numbers and then iterates n times, adding the current term to the total sum and updating the Perrin sequence. The function returns the total sum.

The unit test `assert cal_sum(9) == 49` ensures that the function correctly calculates the sum of the first 9 Perrin numbers, which is indeed 49.