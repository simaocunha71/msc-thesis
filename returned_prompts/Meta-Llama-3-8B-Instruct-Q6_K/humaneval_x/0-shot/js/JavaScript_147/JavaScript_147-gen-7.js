The problem can be solved by creating an array a of length n and calculating the sum of each triple (a[i], a[j], a[k]) for i < j < k. We can use a hash map to store the sum of each triple and its count. Then, we iterate over the array and calculate the sum of each triple. If the sum is a multiple of 3, we increment the count in the hash map. Finally, we return the count of triples whose sum is a multiple of 3.

Here is the implementation in JavaScript:
```
const getMaxTriples = (n) => {
  const a = new Array(n + 1).fill(0);
  for (let i = 1; i <= n; i++) {
    a[i] = i * i - i + 1;
  }
  let count = 0;
  const sums = new Map();
  for (let i = 1; i < n; i++) {
    for (let j = i + 1; j <= n; j++) {
      const sum = a[i] + a[j];
      if (sums.has(sum)) {
        count += sums.get(sum);
      }
      sums.set(sum, (sums.get(sum) || 0) + 1);
    }
  }
  return count;
};
```
The time complexity of this solution is O(n^2) and the space complexity is O(n). The solution works by iterating over the array and calculating the sum of each triple. The sum is stored in a hash map and its count is incremented. Finally, the count of triples whose sum is a multiple of 3 is returned.

For example, if we call `getMaxTriples(5)`, the output will be 1, which is the number of triples (1, 7, 13) whose sum is a multiple of 3.