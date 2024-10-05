```
def triples_sum_to_zero(l: list):
    seen = set()
    for i in l:
        if i * -1 in seen:
            return True
        seen.add(i)
    return False
```
This solution uses a set `seen` to keep track of the elements we have seen so far. For each element `i` in the list, we check if `-i` is in `seen`. If it is, that means we have found three elements that sum to zero, so we return `True`. If we get through the entire list without finding three elements that sum to zero, we return `False`. The time complexity is O(n), where n is the length of the list, because we are doing a single pass through the list. The space complexity is also O(n), because in the worst case we might have to store every element in the set. 