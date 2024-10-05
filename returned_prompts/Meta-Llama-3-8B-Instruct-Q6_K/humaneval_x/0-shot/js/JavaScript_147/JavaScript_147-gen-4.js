```
function getMaxTriples(n) {
  const a = new Array(n + 1).fill(0);
  let count = 0;
  for (let i = 1; i <= n; i++) {
    a[i] = i * i - i + 1;
  }
  for (let i = 1; i <= n; i++) {
    for (let j = i + 1; j <= n; j++) {
      for (let k = j + 1; k <= n; k++) {
        if ((a[i] + a[j] + a[k]) % 3 === 0) {
          count++;
        }
      }
    }
  }
  return count;
}
```


Explanation:

1. We create an array `a` of size `n + 1` and fill it with zeros.
2. We then calculate the values for `a[i]` for each `i` from 1 to `n` using the formula `i * i - i + 1`.
3. We initialize a variable `count` to 0, which will store the number of triples that satisfy the condition.
4. We use three nested loops to iterate over all possible combinations of `i`, `j`, and `k` such that `i < j < k`.
5. For each combination, we check if the sum `a[i] + a[j] + a[k]` is a multiple of 3. If it is, we increment the `count` variable.
6. Finally, we return the `count` variable, which represents the number of triples that satisfy the condition.

Time complexity: O(n^3)
Space complexity: O(n)

Note: The above solution has a time complexity of O(n^3) due to the three nested loops. This may not be efficient for large values of `n`. A more efficient solution can be achieved by using a different approach, such as using a hash map to store the values of `a[i]` and then iterating over the hash map to find the triples that satisfy the condition. However, this would require a significant change in the code.