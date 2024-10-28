
    def get_max_triples(n):
        count = 0
        a = [i * i - i + 1 for i in range(1, n + 1)]
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (a[i] + a[j] + a[k]) % 3 == 0:
                        count += 1
        return count

print(get_max_triples(5)) # Outputs: 1

This solution works by first generating the list a using the formula provided in the question. Then it goes through all possible triples of indices i, j, k, and checks if the sum of the elements at those indices is a multiple of 3. If it is, it increments the count. Finally, it returns the count.

This solution has a time complexity of O(n^3) which is not efficient for large values of n. A more efficient solution would involve calculating the sum of the elements at each index modulo 3, and then using these results to count the number of valid triples. This would reduce the time complexity to O(n^2).

Here's a more efficient solution:

```python
def get_max_triples(n):
    count = 0
    a = [i * i - i + 1 for i in range(1, n + 1)]
    sum_mod_3 = [0] * 3
    for num in a:
        sum_mod_3[num % 3] += 1
    count += sum_mod_3[0] * (sum_mod_3[0] - 1) * (sum_mod_3[0] - 2) // 6
    count += sum_mod_3[1] * (sum_mod_3[1] - 1) // 2 * sum_mod_3[2]
    count += sum_mod_3[2] * (sum_mod_3[2] - 1) // 2 * sum_mod_3[1]
    return count
```

This solution works by first counting the number of elements in a that are congruent to 0, 1, and 