```
def pairs_sum_to_zero(l):
    if len(l) < 2:
        return False
    
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False
```

This function uses a set `seen` to keep track of the numbers we have seen so far. For each number in the list, it checks if its negation is in `seen`. If it is, then we have found two distinct elements that sum to zero, and the function returns `True`. If we finish iterating over the list without finding such a pair, the function returns `False`. The time complexity of this function is O(n), where n is the length of the input list, because it makes a single pass through the list. The space complexity is also O(n), because in the worst case (when all numbers are distinct) it will store all numbers in the `seen` set. 