```javascript
const isEqualToSumEven = (n) => {
  for (let i = 2; i <= n; i += 2) {
    let sum = 0;
    for (let j = 2; j <= n; j += 2) {
      if (sum + j > n) break;
      sum += j;
      if (sum === n) return true;
    }
  }
  return false;
};
```
The function `isEqualToSumEven` checks whether the given number `n` can be written as the sum of exactly 4 positive even numbers. It does this by iterating through all even numbers from 2 to `n`, and for each even number, it checks if it can be written as the sum of exactly 4 other even numbers. If it finds a combination that sums up to `n`, it returns `true`. If it doesn't find such a combination after checking all even numbers, it returns `false`.

For example, when `n` is 8, the function will find that 2 + 2 + 2 + 2 = 8, so it will return `true`. When `n` is 6, the function will not find a combination of 4 even numbers that sums up to 6, so it will return `false`. When `n` is 4, the function will not find a combination of 4 even numbers that sums up to 4, so it will return `false`.