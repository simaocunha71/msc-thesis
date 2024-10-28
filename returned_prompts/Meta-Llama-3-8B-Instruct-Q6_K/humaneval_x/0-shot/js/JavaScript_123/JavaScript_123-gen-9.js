```
const getOddCollatz = (n) => {
  const sequence = [n];
  while (n !== 1) {
    if (n % 2 === 0) {
      n = Math.floor(n / 2);
    } else {
      n = n * 3 + 1;
    }
    sequence.push(n);
  }
  const oddNumbers = sequence.filter(num => num % 2 !== 0);
  return oddNumbers.sort((a, b) => a - b);
};
```


Explanation:

1. We start by creating an array `sequence` and adding the input `n` to it.
2. We then enter a while loop that continues until `n` becomes 1.
3. Inside the loop, we check if `n` is even by using the modulus operator `%`. If it is even, we divide it by 2. If it is odd, we multiply it by 3 and add 1.
4. We add each resulting `n` value to the `sequence` array.
5. Once the loop ends, we filter the `sequence` array to keep only the odd numbers using the `filter` method and the condition `num % 2 !== 0`.
6. Finally, we sort the filtered array in increasing order using the `sort` method and return it.

For example, if we call `getOddCollatz(5)`, the function will return the array `[1, 5]`, which are the odd numbers in the Collatz sequence for 5.