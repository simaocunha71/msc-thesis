```
def triples_sum_to_zero(l: list):
    seen = set()
    for num in l:
        if num in seen:
            continue
        seen.add(num)
        for other_num in l:
            if num == other_num:
                continue
            complement = -num - other_num
            if complement in seen:
                return True
    return False
```

The function `triples_sum_to_zero` takes a list of integers as an input and returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise.

The function uses a set `seen` to keep track of the numbers that have been seen so far. It iterates over the list of numbers, and for each number, it checks if there are two other numbers in the list that sum to the negation of the current number. If it finds such a pair, it returns `True`. If it does not find any such pair after iterating over the entire list, it returns `False`.

The time complexity of this function is O(n^2), where n is the length of the input list. This is because it iterates over the list once, and for each number, it iterates over the list again to find the pair of numbers that sum to the negation of the current number. The space complexity is O(n), where n is the length of the input list, because it uses a set to keep track of the numbers that have been seen so far.