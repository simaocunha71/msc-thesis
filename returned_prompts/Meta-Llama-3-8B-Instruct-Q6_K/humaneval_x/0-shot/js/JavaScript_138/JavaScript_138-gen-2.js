```javascript
const isEqualToSumEven = (n) => {
  for (let i = 2; i <= n; i += 2) {
    let sum = 0;
    for (let j = 2; j <= n; j += 2) {
      if (i + j <= n) {
        sum += i + j;
        if (sum === n) {
          return true;
        }
      } else {
        break;
      }
    }
  }
  return false;
};
```


The function `isEqualToSumEven` takes an integer `n` as input and checks whether it can be written as the sum of exactly 4 positive even numbers. It does this by iterating through all possible pairs of even numbers up to `n` and checking if their sum equals `n`. If it finds such a pair, it returns `true`. If it doesn't find any such pair, it returns `false`.

In the code above, we use two nested for loops to iterate through all possible pairs of even numbers up to `n`. The outer loop iterates through the even numbers from 2 to `n`, and the inner loop iterates through the even numbers from 2 to `n` (but not exceeding the sum of the current pair). If the sum of the current pair exceeds `n`, we break out of the inner loop. If the sum of the current pair equals `n`, we return `true`. If we finish iterating through all pairs without finding a pair that sums up to `n`, we return `false`.

This solution has a time complexity of O(n^2), where `n` is the input number. This is because we iterate through all possible pairs of even numbers up to `n`, which takes O(n) time, and for each pair, we check whether its sum equals `n`, which takes O(1) time. The space complexity is O(1), as we only use a constant amount of space to store the sum and the current pair of even numbers.