Here is a JavaScript function that solves the problem:

```javascript
const isEqualToSumEven = (n) => {
  for (let a = 2; a <= n; a += 2) {
    for (let b = 2; b <= n; b += 2) {
      for (let c = 2; c <= n; c += 2) {
        for (let d = 2; d <= n; d += 2) {
          if (a + b + c + d === n) {
            return true;
          }
        }
      }
    }
  }
  return false;
};
```

This function iterates over all possible combinations of four even numbers, and checks if their sum equals the given number `n`. If it finds such a combination, it returns `true`. If it doesn't find any combination after checking all possibilities, it returns `false`.

Note that this function is not very efficient for large numbers, as it has a time complexity of O(n^4). For large numbers, a more efficient solution would be needed. For example, we could use a more efficient algorithm to find the sum of four even numbers, or we could use a hash table to store the sums of smaller even numbers and check if the given number is equal to the sum of four such sums. However, for small numbers, this function should work fine.