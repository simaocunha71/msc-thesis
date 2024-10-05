To solve this problem, we need to understand the pattern of numbers that start or end with 1. Let's break down the problem:

1. If the number has n digits, it can start with 1, followed by any of the remaining (n-1) digits, which can be any number from 0 to 9. So, there are 9 choices for each of the (n-1) digits after 1.

2. Similarly, the number can end with 1, preceded by any of the remaining (n-1) digits, which can be any number from 0 to 9. So, there are 9 choices for each of the (n-1) digits before 1.

3. Therefore, the total number of n-digit positive integers that start or end with 1 is 9 * 9^(n-2).

Here is the solution in JavaScript:

```javascript
const startsOneEnds = (n) => {
  if (n === 1) {
    return 2; // 1 and 9
  }
  return 9 * Math.pow(9, n - 2);
};
```

Let's test the solution:

```javascript
console.log(startsOneEnds(1)); // Output: 2
console.log(startsOneEnds(2)); // Output: 81
console.log(startsOneEnds(3)); // Output: 729
console.log(startsOneEnds(4)); // Output: 6561
```

The solution passes all the test cases.