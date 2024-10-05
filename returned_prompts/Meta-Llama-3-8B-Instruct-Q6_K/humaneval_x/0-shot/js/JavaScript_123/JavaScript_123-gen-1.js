Here is the solution:
```javascript
const getOddCollatz = (n) => {
  const sequence = [n];
  while (n !== 1) {
    if (n % 2 === 0) {
      n = Math.floor(n / 2);
    } else {
      n = n * 3 + 1;
    }
    if (!sequence.includes(n)) {
      sequence.push(n);
    }
  }
  return sequence.filter((num) => num % 2 !== 0).sort((a, b) => a - b);
};
```
Here is an explanation of the code:

1. We start with the initial value `n` and create an array `sequence` to store the Collatz sequence.
2. We loop until `n` reaches 1.
3. In each iteration, we check if `n` is even or odd. If it's even, we divide it by 2. If it's odd, we multiply it by 3 and add 1.
4. We check if the new value of `n` is already in the `sequence` array. If not, we add it to the array.
5. Finally, we filter the `sequence` array to keep only the odd numbers and sort them in increasing order.

You can test the function with different values of `n` to see the output. For example, `getOddCollatz(5)` returns `[1, 5]`, which is the expected output.