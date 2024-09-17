```
def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] ^ lst[j]) % 2 == 0:
                count += 1
    return count
```
The function `find_even_pair` takes a list of integers as input and returns the count of pairs of integers that xor to an even number. It uses a nested loop to iterate over all pairs of integers in the list. For each pair, it checks if the result of the xor operation is even by using the modulus operator `%`. If the result is even, it increments the count. Finally, it returns the total count.

The unit test `assert find_even_pair([5, 4, 7, 2, 1]) == 4` ensures that the function works correctly. It checks that the function returns 4, which is the correct count of pairs that xor to an even number in the given list.