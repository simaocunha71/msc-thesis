```
def odd_num_sum(n):
    return sum([i**4 for i in range(1, n*2, 2)])
```
The problem is asking to find the sum of fourth power of first n odd natural numbers. 

The unit test `assert odd_num_sum(2) == 82` helps to understand that we need to consider the first n odd natural numbers. 

The function `odd_num_sum` generates all odd numbers from 1 to 2n-1 using list comprehension and calculates the fourth power of each number. The sum of these fourth powers is then returned.

The unit test `assert odd_num_sum(2) == 82` passes because the sum of the fourth power of the first two odd natural numbers (1 and 3) is 1**4 + 3**4 = 1 + 81 = 82. 