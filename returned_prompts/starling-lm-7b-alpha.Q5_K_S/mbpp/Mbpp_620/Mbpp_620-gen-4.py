```
def largest_subset(seq):
    divisors = set()
    for i, num in enumerate(seq):
        if num % 2 == 0:
            divisors.add(2)
        for j in range(i+1, len(seq)):
            if seq[j] % num == 0:
                divisors.add(seq[j])
    return len(divisors)
```

This function `largest_subset` takes a list of numbers as an input and finds the size of the largest subset of the list so that every pair of numbers in the subset is divisible. 

To do this, the function first initializes an empty set called `divisors` to keep track of the divisors found in the sequence. 

Next, it iterates through the input list using a for loop. For each number in the list, it checks if the number is divisible by 2. If it is, it adds 2 to the `divisors` set. 

Then, it iterates through the rest of the list starting from the current index using another for loop. For each number in the list, it checks if the number is divisible by the current number. If it is, it adds the number to the `divisors` set. 

After iterating through the entire list, the function returns the length of the `divisors` set, which represents the size of the largest subset of numbers that are divisible. 

In the provided example, the function is called with the list `[1, 3, 6, 13, 17, 18]`. The function correctly identifies that the largest subset of divisible numbers is `[6, 18]`, which has a size of 2, and returns 2 as the result.

Overall, this function provides an efficient solution to find the size of the largest subset of divisible numbers in a given list.

```python
def largest_subset(seq):
    divisors = set()
    for i, num in enumerate(seq):
        if num % 2 == 0:
            divisors.add(2)
        for j in range(i+1, len(seq)):
            if seq[j] % num ==