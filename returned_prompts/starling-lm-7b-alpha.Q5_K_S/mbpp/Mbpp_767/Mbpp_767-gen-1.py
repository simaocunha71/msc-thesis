Here's a Python function that counts the number of pairs whose sum is equal to the given sum:

```python
def get_pairs_count(num_list, sum):
    count = 0
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == sum:
                count += 1
    return count
```

You can call this function with a list of numbers and the desired sum to get the count of pairs that add up to that sum. For example, `get_pairs_count([1,1,1,1],2)` will return `6` as there are six pairs of numbers that add up to `2` in the given list.

The function iterates through each pair of numbers in the list using nested loops. It checks if the sum of the current pair of numbers is equal to the desired sum. If it is, it increments the count variable. Finally, it returns the count of pairs that add up to the given sum.

This function has a time complexity of O(n^2) because it checks all possible pairs of numbers in the list.

```python
# Example usage:
num_list = [1, 1, 1, 1]
sum = 2
print(get_pairs_count(num_list, sum))  # Output: 6
```

Please note that this function assumes that the input list does not contain duplicate numbers. If the list can have duplicate numbers, you may need to modify the function to handle duplicates appropriately.

In addition, be aware that this function is case-sensitive. If you want to make it case-insensitive, you can convert the numbers to lowercase (or uppercase) before performing the addition.

Finally, it's worth mentioning that this function only counts pairs that add up to the exact sum provided. If you want to count pairs that add up to within a certain range, you would need to modify the function accordingly.
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