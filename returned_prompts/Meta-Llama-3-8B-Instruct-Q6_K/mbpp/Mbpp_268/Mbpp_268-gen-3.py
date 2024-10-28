The problem is asking to write a function that finds the n'th star number. Star numbers are a sequence of numbers where each number is the sum of the squares of the first n natural numbers.

For example, the first few star numbers are: 0, 1, 4, 9, 25, 49, 81, 121, 169, 225, ...

The unit test `assert find_star_num(3) == 37` suggests that the sequence starts from 0.

Here is the solution:
```
def find_star_num(n):
    if n == 1:
        return 0
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total
```



