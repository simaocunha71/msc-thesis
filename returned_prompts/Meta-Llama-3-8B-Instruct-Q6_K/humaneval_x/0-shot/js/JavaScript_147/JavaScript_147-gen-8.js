The problem is asking to find the number of triples (a[i], a[j], a[k]) in an array a of length n, where i < j < k, and a[i] + a[j] + a[k] is a multiple of 3.

Here is a Python solution for the problem:
```
def maxTriples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count
```
The above code generates the array a of length n and then iterates over all possible triples (a[i], a[j], a[k]). If the sum of the triple is a multiple of 3, it increments the count. Finally, it returns the count.

The time complexity of this solution is O(n^3) because it has three nested loops. The space complexity is O(n) because it stores the array a.

Note that the problem statement does not specify whether the triples should be distinct or not. However, based on the example given, it seems that the triples should be distinct. Therefore, the solution above does not consider duplicate triples. If the problem statement is changed to allow duplicate triples, the solution would be slightly modified.