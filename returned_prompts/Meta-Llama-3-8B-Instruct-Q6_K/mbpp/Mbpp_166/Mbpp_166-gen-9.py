```
def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if (lst[i] ^ lst[j]) % 2 == 0:
                count += 1
    return count
```
The function `find_even_pair` iterates over the list of integers and checks each pair of integers to see if their XOR is even. It does this by using the bitwise XOR operator (`^`) and checking if the result is even by using the modulo operator (`%`) to see if the result is divisible by 2. If the result is even, it increments the count of pairs with even XOR. Finally, it returns the total count of pairs with even XOR. 

The unit test `assert find_even_pair([5, 4, 7, 2, 1]) == 4` ensures that the function is working correctly by checking that the function returns 4 when given the list `[5, 4, 7, 2, 1]`. This is because the pairs `(5, 4)`, `(4, 7)`, `(2, 1)` and `(5, 7)` have even XOR. 

Note: This function has a time complexity of O(n^2) where n is the number of elements in the list, because it uses two nested loops to iterate over the list. This may not be efficient for large lists. A more efficient solution would be to use a hash table to store the elements of the list and their XOR, and then iterate over the hash table to count the pairs with even XOR. This would have a time complexity of O(n). 





