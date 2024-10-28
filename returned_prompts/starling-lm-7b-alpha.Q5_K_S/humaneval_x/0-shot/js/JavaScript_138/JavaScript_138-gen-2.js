To solve this problem, we can use a backtracking algorithm to check whether we can find four even numbers that sum up to n. Here's a step-by-step explanation of the algorithm:

1. Initialize an empty array `sums` to store all the possible sums of the even numbers.
2. Initialize a variable `total` to keep track of the current sum.
3. Define a function `checkSum` that takes a number `n` and an index `i` as arguments. This function checks if the sum of the first `i` numbers in the `sums` array is equal to `n`. If it is, return true. If the sum is less than `n`, call the `checkSum` function recursively with the next number in the `sums` array. If the sum is greater than `n`, return false.
4. In the main function, iterate through all the even numbers from 2 to `n`. For each even number, add it to the `sums` array and increment `total` by the even number. After adding the even number to the `sums` array, call the `checkSum` function with the current `total` and the length of the `sums` array. If `checkSum` returns true, return true. If `checkSum` returns false and we have iterated through all the even numbers, return false.
5. If the main function returns true, it means that there exist four even numbers that sum up to `n`. Otherwise, return false.

Here's the implementation of the algorithm in JavaScript:

```javascript
function isEqualToSumEven(n) {
  let sums = [];
  let total = 0;
  
  function checkSum(n, i) {
    if (sums[i] === n) return true;
    if (sums[i] > n) return false;
    return checkSum(n, i + 1);
  }
  
  for (let i = 2; i <= n; i += 2) {
    sums.push(i);
    total += i;
    if (checkSum(total, sums.length)) {
      return true;
    }
  }
  
  return false;
}
```

You can use this