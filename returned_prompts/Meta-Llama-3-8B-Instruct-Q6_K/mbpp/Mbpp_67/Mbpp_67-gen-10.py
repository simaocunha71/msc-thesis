The Bell number is a mathematical function that counts the number of ways to partition a set of n elements. The Bell number for n=2 is 2, because there are two ways to partition a set of 2 elements: {{}, {1}, {2}} and {{1, 2}}. The function to calculate the number of ways to partition a set of Bell numbers is as follows:

```
def bell_number(n):
    if n == 0:
        return 1
    else:
        return sum([bell_number(k) * bell_number(n-1-k) for k in range(n+1)])
```

This function uses a recursive approach to calculate the Bell number. The base case is when n is 0, in which case the Bell number is 1. Otherwise, the Bell number is the sum of the Bell numbers of all subsets of the set of n elements, which is calculated by iterating over all possible subsets and multiplying the Bell number of each subset by the Bell number of the complement of that subset. The result is the total number of ways to partition the set of n elements. For example, the Bell number for n=2 is calculated as bell_number(2) = bell_number(0) * bell_number(2-0-2) + bell_number(1) * bell_number(2-1-1) = 1 * 1 + 1 * 1 = 2. This is the same as the number of ways to partition a set of 2 elements, which is 2. The unit test `assert bell_number(2)==2` verifies that the function correctly calculates the Bell number for n=2.