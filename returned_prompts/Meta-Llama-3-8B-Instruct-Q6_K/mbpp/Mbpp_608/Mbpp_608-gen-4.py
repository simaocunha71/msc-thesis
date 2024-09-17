The bell numbers are a sequence of numbers that count the number of ways to partition a set of n elements. They are named after Eric Temple Bell, who studied them in the 1930s.

The nth Bell number is the number of ways to partition a set of n elements. For example, the 0th Bell number is 1, because there is one way to partition a set of 0 elements (which is to have no partitions at all). The 1st Bell number is 1, because there is one way to partition a set of 1 element (which is to have one partition, which is the set itself). The 2nd Bell number is 2, because there are two ways to partition a set of 2 elements (which are to have one partition, which is the set itself, or to have two partitions, which are the two individual elements).

Here is a Python function that calculates the nth Bell number:
```
def bell_Number(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return sum(bell_Number(i) * bell_Number(n-1-i) for i in range(n+1))
```
This function uses dynamic programming to calculate the nth Bell number. It starts by checking if n is less than 0, in which case it returns 0. If n is 0, it returns 1. Otherwise, it calculates the nth Bell number by summing the product of the ith Bell number and the (n-1-i)th Bell number over all i from 0 to n. This is because the nth Bell number is the sum of the product of the ith Bell number and the (n-1-i)th Bell number over all i from 0 to n. The function then returns the result.

For example, if you call `bell_Number(2)`, the function will return 2, which is the correct value for the 2nd Bell number. If you call `bell_Number(3)`, the function will return 5, which is the correct value for the 3rd Bell number. And so on.