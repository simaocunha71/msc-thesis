```
def count_Pairs(lst, n):
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] != lst[j]:
                pairs += 1
    return pairs
```
This function takes a list of integers and an integer `n` as input. It initializes a variable `pairs` to 0, which will count the number of possible unordered pairs where both elements are unequal. It then uses two nested loops to iterate over the list. For each pair of elements, it checks if they are unequal and increments the `pairs` variable if they are. Finally, it returns the total count of pairs. The unit test `assert count_Pairs([1,2,1],3) == 2` confirms that the function works correctly. 

The time complexity of this function is O(n^2) because it uses two nested loops to iterate over the list. The space complexity is O(1) because it only uses a constant amount of space to store the `pairs` variable and the loop indices. 

Note that the input `n` is not actually used in the function, so it could be removed. The function would still work correctly without it. The unit test could also be modified to use a list of length `n` instead of a specific value. For example, `assert count_Pairs([1,2,1,2],4) == 4`. 

Alternatively, the function could be written in a more concise way using the `itertools` module and a generator expression:
```
import itertools

def count_Pairs(lst):
    return sum(1 for i, j in itertools.combinations(lst, 2) if i != j)
```
This function uses the `combinations` function from the `itertools` module to generate all possible pairs of elements from the list. It then uses a generator expression to count the number of pairs where the elements are unequal. The `sum` function is used to calculate the total count. This function has the same time and space complexity as the original function. 

The unit test `assert count_Pairs([1,2,1]) == 2` confirms that this function works correctly. 

Note that this function assumes that the input list has at least two elements. If the input list has only one element, the function will return 0. If the input list is empty, the function will raise a `ValueError`. 

To handle these