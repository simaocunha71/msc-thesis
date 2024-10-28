```
def pair_wise(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            result.append((lst[i], lst[j]))
    return result
```


Explanation:
The problem is asking for a function that takes a list as input and returns a list of all pairs of consecutive items in the given list.

The unit test `assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]` helps to understand the problem better. It shows that consecutive items are considered as any two items in the list that are adjacent to each other.

The solution uses two nested loops to generate all pairs of consecutive items in the list. The outer loop iterates over each item in the list, and the inner loop iterates over the remaining items in the list, starting from the next item after the current item. The pair of consecutive items is then added to the result list.

The time complexity of this solution is O(n^2), where n is the length of the input list, because it uses two nested loops to generate all pairs of consecutive items. The space complexity is O(n^2) as well, because it stores all pairs of consecutive items in the result list. 