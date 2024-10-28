```
def count_Pairs(lst, k):
    count = 0
    seen = set()
    for num in lst:
        for other in seen:
            if num != other and num <= k:
                count += 1
        seen.add(num)
    return count
```
The function count_Pairs takes a list of integers and an integer k as input, and returns the number of possible unordered pairs where both elements are unequal and less than or equal to k.

The function iterates over the list and for each element, it iterates over the set of elements it has seen so far. If the current element is unequal to the other element and less than or equal to k, it increments the count.

Finally, it adds the current element to the set of elements it has seen so far.

The unit test `assert count_Pairs([1,2,1],3) == 2` ensures that the function works correctly. It checks that the function returns 2 for the input [1,2,1] and k=3, which is the correct count of possible unordered pairs where both elements are unequal and less than or equal to 3. 