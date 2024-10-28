```js
const getOddCollatz = (n) => {
  const collatz = [n];
  while (n !== 1) {
    n = n % 2 === 0 ? n / 2 : 3 * n + 1;
    collatz.push(n);
  }
  return collatz.filter(x => x % 2 !== 0).sort((a, b) => a - b);
}
```

This solution first generates the collatz sequence starting from the given number `n`. It keeps generating the next number in the sequence until it reaches 1. Then, it filters out the even numbers from the sequence and sorts the remaining odd numbers in ascending order. Finally, it returns the sorted list of odd numbers in the collatz sequence.