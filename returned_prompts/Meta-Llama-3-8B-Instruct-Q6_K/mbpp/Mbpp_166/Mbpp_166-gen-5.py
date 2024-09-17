```
def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if (lst[i] ^ lst[j]) % 2 == 0:
                count += 1
    return count
```
The function `find_even_pair` takes a list of integers as input and returns the count of pairs of integers in the list that have an even XOR. The function uses a nested loop to iterate over all pairs of integers in the list. For each pair, it checks if the XOR of the two integers is even by using the modulo operator (`%`). If the result is 0, it increments the count. Finally, the function returns the total count. The unit test `assert find_even_pair([5, 4, 7, 2, 1]) == 4` ensures that the function is working correctly. 