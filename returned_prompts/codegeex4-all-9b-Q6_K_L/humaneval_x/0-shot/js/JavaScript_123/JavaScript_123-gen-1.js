```
const getOddCollatz = (n) => {
  let arr = [n];
  while (n > 1) {
    n = (n % 2 === 0) ? n / 2 : n * 3 + 1;
    if (n % 2 === 1) arr.push(n);
  }
  return arr.sort((a, b) => a - b);
}
```
Explanation:
1. Initialize the array with the given number `n`.
2. While `n` is greater than 1, calculate the next number in the sequence.
3. If the next number is odd, add it to the array.
4. Sort the array in ascending order and return it.