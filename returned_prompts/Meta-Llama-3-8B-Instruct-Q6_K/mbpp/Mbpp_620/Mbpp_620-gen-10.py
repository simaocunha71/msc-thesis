```
def largest_subset(lst):
    if len(lst) == 1:
        return 1
    if len(lst) == 2:
        return 1 if lst[0] % lst[1] == 0 or lst[1] % lst[0] == 0 else 0

    max_size = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] % lst[j] == 0 or lst[j] % lst[i] == 0:
                subset = [lst[i], lst[j]]
                size = 1
                for k in range(len(lst)):
                    if k not in (i, j) and lst[i] % lst[k] == 0 or lst[k] % lst[i] == 0:
                        subset.append(lst[k])
                        size += 1
                max_size = max(max_size, size)

    return max_size
```


The problem is asking to find the size of the largest subset of a list of numbers where every pair of numbers is divisible. 

The solution uses a brute force approach by checking every pair of numbers in the list and then checking if the remaining numbers in the list are also divisible by any of the numbers in the pair. The maximum size of such a subset is returned.

The unit test `assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4` helps to clarify the problem by providing an example of a list of numbers and the expected size of the largest subset.

However, this solution is not efficient for large lists of numbers because it has a time complexity of O(n^2) where n is the length of the list. A more efficient solution would be to use a data structure such as a hash table to store the divisors of each number and then use this information to build the largest subset. This would reduce the time complexity to O(n). 

Here is a more efficient solution:

```
def largest_subset(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    max_size = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] % lst[j] == 0 or lst[j] % lst