```
const getOddCollatz = (n) => {
  const collatzSequence = [n];
  while (n !== 1) {
    if (n % 2 === 0) {
      n = Math.floor(n / 2);
    } else {
      n = n * 3 + 1;
    }
    collatzSequence.push(n);
  }
  return collatzSequence.filter((num) => num % 2 !== 0).sort((a, b) => a - b);
};
```


Explanation:
1. Initialize an array `collatzSequence` with the input number `n`.
2. Loop until `n` becomes 1.
3. In each iteration, check if `n` is even or odd. If even, divide `n` by 2. If odd, multiply `n` by 3 and add 1.
4. Add the updated `n` to the `collatzSequence` array.
5. Once `n` becomes 1, filter the `collatzSequence` array to keep only the odd numbers using the `filter()` method with a callback function that checks if a number is odd (`num % 2 !== 0`).
6. Sort the filtered array in ascending order using the `sort()` method with a comparison function that returns the difference between two numbers (`a - b`).
7. Return the sorted array of odd Collatz sequence numbers.

Example:
```
getOddCollatz(5) // [1, 5]
```
The Collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are 1 and 5. The function returns a sorted array of these odd numbers: [1, 5].