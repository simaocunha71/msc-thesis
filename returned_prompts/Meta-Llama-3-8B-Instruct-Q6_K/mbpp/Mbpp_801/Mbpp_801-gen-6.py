```
def count_equal_numbers(a, b, c):
    count = 0
    if a == b:
        count += 1
    if a == c:
        count += 1
    if b == c:
        count += 1
    return count
```


This function takes three integers as input and returns the count of equal numbers. It uses if-else conditions to check for equality between the numbers. If a number is equal to another, it increments the count. Finally, it returns the count. The unit test `assert test_three_equal(1,1,1) == 3` ensures that the function works correctly when all the numbers are equal. 
However, this solution is not very efficient as it has to make three comparisons. A more efficient solution would be to use a set to count the unique numbers and then subtract this from the total count of numbers to get the count of equal numbers. But this solution is more complex and may be harder to understand for beginners. 

Here is the efficient solution:

```
def count_equal_numbers(a, b, c):
    total_count = 3
    unique_count = len(set([a, b, c]))
    return total_count - unique_count + 1
```

This function works by first initializing a total count of 3 (since there are three numbers). Then it uses a set to count the unique numbers. The length of the set is the number of unique numbers. The total count minus the unique count plus one gives the count of equal numbers. This solution is more efficient because it only needs to make one comparison to get the unique count. 