Here is the solution using recursion:

```javascript
const getOddCollatz = (n) => {
  const collatz = [n];
  while (n !== 1) {
    if (n % 2 === 0) {
      n = Math.floor(n / 2);
    } else {
      n = n * 3 + 1;
    }
    collatz.push(n);
  }
  return collatz.filter((num) => num % 2 !== 0).sort((a, b) => a - b);
};
```

Here is the explanation:

1. We start with an array `collatz` that contains the initial number `n`.
2. We enter a while loop that continues until `n` becomes 1.
3. Inside the loop, we check if `n` is even or odd. If it's even, we divide it by 2; if it's odd, we multiply it by 3 and add 1.
4. We add the new value of `n` to the `collatz` array.
5. Once the loop ends, we filter the `collatz` array to keep only the odd numbers using the `filter` method with a predicate that checks if a number is odd (`num % 2 !== 0`).
6. We sort the filtered array in ascending order using the `sort` method with a compare function that subtracts two numbers (`a - b`).
7. The resulting array is the sorted list of odd numbers in the Collatz sequence.

For example, if we call `getOddCollatz(5)`, the function will return the array `[1, 5]`, which are the odd numbers in the Collatz sequence for 5.