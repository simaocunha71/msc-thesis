Let's first generate all the n-digit positive integers. We can do this by generating all the numbers from 10^(n-1) to 10^n - 1. Then, for each number, we check if it starts or ends with 1. If it does, we increment the count.

Here's the code in JavaScript:
```
const startsOneEnds = (n) => {
  let count = 0;
  for (let i = Math.pow(10, n - 1); i < Math.pow(10, n); i++) {
    const str = i.toString();
    if (str.startsWith('1') || str.endsWith('1')) {
      count++;
    }
  }
  return count;
};
```
This function works by iterating over all n-digit numbers and checking if they start or end with 1. It uses the `startsWith` and `endsWith` methods to check if the number starts or ends with 1, and increments the count accordingly.

For example, if n is 2, the function would iterate over the numbers 10, 11, 12, ..., 99. It would find that 11, 12, 19, 21, 91, and 99 start or end with 1, so the count would be 6.

The time complexity of this function is O(10^n), because we are iterating over all n-digit numbers. The space complexity is O(1), because we only use a constant amount of space to store the count and the current number. 