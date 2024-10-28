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
  return sequence.filter((num) => num % 2 !== 0).sort((a, b) => a - b);
};
```


Explanation:
This function generates the Collatz sequence for the given number `n` and filters out the even numbers. Then it sorts the remaining odd numbers in ascending order.

1. Initialize the sequence with the given number `n`.
2. Loop until `n` becomes 1. In each iteration:
   - If `n` is even, divide it by 2.
   - If `n` is odd, multiply it by 3 and add 1.
   - Add `n` to the sequence.
3. Filter the sequence to keep only the odd numbers using the `filter()` method and the condition `num % 2 !== 0`.
4. Sort the filtered sequence in ascending order using the `sort()` method and the comparison function `(a, b) => a - b`.
5. Return the sorted sequence of odd numbers.