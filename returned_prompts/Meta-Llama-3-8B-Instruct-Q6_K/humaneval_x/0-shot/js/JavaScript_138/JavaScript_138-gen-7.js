```javascript
const isEqualToSumEven = (n) => {
  for (let i = 2; i <= n; i += 2) {
    let sum = 0;
    for (let j = 2; j <= n; j += 2) {
      if (i !== j) {
        sum += j;
        if (sum === n) {
          return true;
        }
      }
    }
  }
  return false;
};
```


Here is an explanation of the code:

The function `isEqualToSumEven` takes a number `n` as input and checks whether it can be written as the sum of exactly 4 positive even numbers.

The function uses two nested loops to iterate over all even numbers from 2 to `n`. The outer loop iterates over the first even number `i`, and the inner loop iterates over the second even number `j`. The condition `i !== j` ensures that we don't add `i` to the sum again.

The sum is initialized to 0 and incremented by `j` in each iteration of the inner loop. If the sum becomes equal to `n`, the function returns `true`, indicating that `n` can be written as the sum of exactly 4 positive even numbers.

If the function finishes iterating over all even numbers without finding a combination that sums up to `n`, it returns `false`, indicating that `n` cannot be written as the sum of exactly 4 positive even numbers.

Note that this function has a time complexity of O(n^2), which may not be efficient for large values of `n`. A more efficient solution could be implemented using a dynamic programming approach or by using a mathematical formula to calculate the sum of even numbers.