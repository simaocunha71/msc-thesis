
Here's a step by step guide on how to solve this problem:

1. Create an array called `collatz` and initialize it with the value of `n`. This array will hold all the numbers in the Collatz sequence.

2. Create an array called `odds` and initialize it with the value of `n`. This array will hold all the odd numbers in the Collatz sequence.

3. Create a `while` loop that runs until the value of `n` is equal to 1. Inside the loop, check if the value of `n` is odd. If it is, add `n` to the `odds` array. If it's not, add `n` to the `collatz` array. Then, calculate the next value of `n` based on the Collatz sequence rules.

4. After the loop, sort the `odds` array in increasing order and return it.

Here's the code that implements these steps:

```javascript
const getOddCollatz = (n) => {
  let collatz = [n];
  let odds = [n];

  while (n !== 1) {
    if (n % 2 === 1) {
      odds.push(n);
    } else {
      collatz.push(n);
    }
    n = n % 2 === 1 ? 3 * n + 1 : n / 2;
  }

  odds.sort((a, b) => a - b);
  return odds;
};
```

This code defines a function called `getOddCollatz` that takes a positive integer `n` as an argument. It initializes two arrays `collatz` and `odds` with the value of `n`. It then enters a `while` loop that continues until `n` equals 1. Inside the loop, it checks if `n` is odd, and if so, adds it to the `odds` array. If `n` is even, it adds it to the `collatz` array. It then calculates the next value of `n` based on the Collatz sequence rules. After the loop, it sorts the `odds` array in increasing order and returns it.

For example, if you call `getOdd