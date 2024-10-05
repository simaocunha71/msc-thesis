```js
const getOddCollatz = (n) => {
  let odd = [];
  while (n !== 1) {
    if (n % 2 === 1) {
      odd.push(n);
    }
    n = n % 2 === 0 ? n / 2 : 3 * n + 1;
  }
  odd.push(1);
  return odd.sort((a, b) => a - b);
}
```
The above solution works by iterating through the Collatz sequence of the given number and adding each odd number encountered to an array. Once the sequence reaches 1, the array is sorted in ascending order and returned.

The main logic is in the while loop, where we check if the current number is odd, and if so, add it to the array. Then, we update the number according to the Collatz rules: if the number is even, we divide it by 2, and if it's odd, we multiply it by 3 and add 1.

Finally, we add 1 to the array and return it sorted in ascending order.