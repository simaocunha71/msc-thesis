
To solve this problem, we can start by analyzing the array a that is created based on the given formula. We know that a[i] = i * i - i + 1. Let's find the first few elements of the array:

For i = 1: a[1] = 1
For i = 2: a[2] = 4
For i = 3: a[3] = 9
For i = 4: a[4] = 16
For i = 5: a[5] = 25

From this, we can see that every element of the array is either divisible by 3 or has a remainder of 2 when divided by 3. This means that if the sum of any three elements of the array is divisible by 3, then at least one of the elements must have a remainder of 0 when divided by 3.

To count the number of triples (a[i], a[j], a[k]) that satisfy the condition, we can use a simple counting approach. We can iterate through all possible combinations of indices (i, j, k) and check if the sum of the corresponding elements is divisible by 3. We can keep a count of the satisfying triples and return it as the result.

Here's the Python code to implement this approach:

```python
def get_max_triples(n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count
```

In the above code, we use three nested loops to iterate through all possible combinations of indices (i, j, k). We check if the sum of the corresponding elements (a[i], a[j], a[k]) is divisible by 3 using the modulo operator (%). If it is, we increment the count variable.

Finally, we return the count as the result.

This approach has a time complexity of O(n^3) due to the nested loops. However, since the input size (n) is