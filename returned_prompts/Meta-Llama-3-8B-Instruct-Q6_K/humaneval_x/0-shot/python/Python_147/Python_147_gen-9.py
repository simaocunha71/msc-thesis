```
def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n+1)]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count
```
Explanation:
The function `get_max_triples(n)` generates an array `a` of length `n` using the given formula. Then, it iterates over all possible triples `(a[i], a[j], a[k])` of the array, checking if the sum `a[i] + a[j] + a[k]` is a multiple of 3. If it is, it increments the count. Finally, it returns the count.

Note: This function has a time complexity of O(n^2) and a space complexity of O(n), where n is the input number. This is because it generates an array of length n and then iterates over all possible triples of the array. The space complexity is O(n) because it stores the array. The time complexity is O(n^2) because it has three nested loops that each iterate n times. This makes the function inefficient for large inputs. A more efficient solution could be found by using mathematical properties of the formula to reduce the number of iterations. For example, it might be possible to use a hash table to store the sums of pairs of elements and then iterate over the array only once to find the triples that sum to a multiple of 3. This would reduce the time complexity to O(n). However, this would also increase the space complexity to O(n) because of the hash table. A compromise could be to use a combination of mathematical properties and hash tables to achieve a better time-space tradeoff.