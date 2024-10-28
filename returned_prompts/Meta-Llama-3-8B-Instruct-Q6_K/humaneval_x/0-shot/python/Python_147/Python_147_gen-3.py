```
def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count
```
This solution first creates the array a according to the given formula. Then, it uses three nested loops to check all possible triples (a[i], a[j], a[k]) of a where i < j < k. If a[i] + a[j] + a[k] is a multiple of 3, it increments the count. Finally, it returns the count. 

The time complexity of this solution is O(n^3) and the space complexity is O(n), where n is the input integer. This is because we need to iterate over all possible triples of the array and the array itself takes O(n) space. 

For larger inputs, this solution may be slow. A more efficient solution would be to use a hash table to store the sum of each pair of elements and then check if the sum of the hash table values is a multiple of 3. This would reduce the time complexity to O(n^2). However, the space complexity would still be O(n). 

Here is the improved solution:

```
def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    hash_table = {}
    for i in range(n):
        for j in range(i + 1, n):
            sum_ij = a[i] + a[j]
            if sum_ij % 3 == 0:
                if sum_ij // 3 in hash_table:
                    count += hash_table[sum_ij // 3]
            if sum_ij not in hash_table:
                hash_table[sum_ij] = 0
            hash_table[sum_ij] += 1
    return count
``` 





Note: This problem is a variation of the "3Sum" problem, where instead of finding all triplets that sum to 0, we need to find all triplets that sum to a multiple of 3. The solution is similar, but with some modifications to handle the new