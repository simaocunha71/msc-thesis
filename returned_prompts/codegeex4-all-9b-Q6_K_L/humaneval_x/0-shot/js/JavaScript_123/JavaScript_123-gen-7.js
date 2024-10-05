```js
const getOddCollatz = (n) => {
  if (n === 1) return [1];
  const sequence = [n];
  while (n !== 1) {
    n = (n % 2 === 0) ? n / 2 : 3 * n + 1;
    if (n % 2 !== 0) sequence.push(n);
  }
  return sequence.sort((a, b) => a - b);
}
```

Explanation:
This function generates the Collatz sequence for a given positive integer n, and returns the odd numbers in the sequence in ascending order.

The function starts by checking if n is equal to 1. If it is, it returns an array with the single element 1.

If n is not equal to 1, the function initializes an array called sequence with the first element being n.

The function then enters a while loop that continues until n is equal to 1. In each iteration of the loop, the function calculates the next number in the Collatz sequence based on whether n is even or odd. If n is even, the next number is n divided by 2. If n is odd, the next number is 3 times n plus 1. The function then checks if the next number is odd, and if it is, it adds it to the sequence array.

Finally, the function returns the sequence array after sorting it in ascending order.