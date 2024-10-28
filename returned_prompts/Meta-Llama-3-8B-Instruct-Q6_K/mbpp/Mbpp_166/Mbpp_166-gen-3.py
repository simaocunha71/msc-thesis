```
def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if (lst[i] ^ lst[j]) % 2 == 0:
                count += 1
    return count
```
This function iterates over each pair of integers in the list and checks if their XOR is even. If it is, it increments the count. The function then returns the total count.

The unit test `assert find_even_pair([5, 4, 7, 2, 1]) == 4` suggests that the function should return 4, which means that there are 4 pairs of integers in the list that XOR to an even number. For example, the pairs (5, 4) and (7, 2) both XOR to an even number. The function correctly identifies these pairs and returns the count of 4.