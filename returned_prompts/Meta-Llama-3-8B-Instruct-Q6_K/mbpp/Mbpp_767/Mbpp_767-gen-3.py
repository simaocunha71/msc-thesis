```
def get_pairs_count(lst, sum):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == sum:
                count += 1
    return count
```
This function iterates over the list and checks for each pair of elements whether their sum is equal to the given sum. If it is, it increments the count. The function finally returns the count.

The unit test `assert get_pairs_count([1,1,1,1],2) == 6` ensures that the function works correctly by checking that for a list of four 1s, there are six pairs whose sum is 2. 

For example, the pairs are (1,1), (1,1), (1,1), (1,1), (1,1), (1,1). The function should return 6 in this case. 

The time complexity of this function is O(n^2) because it uses two nested loops to iterate over the list. The space complexity is O(1) because it only uses a constant amount of space to store the count and the indices. 