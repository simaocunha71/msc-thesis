```javascript
const getOddCollatz = (n) => {
  const collatzSequence = [n];
  let current = n;

  while (current !== 1) {
    if (current % 2 === 0) {
      current = current / 2;
    } else {
      current = current * 3 + 1;
    }
    collatzSequence.push(current);
  }

  return collatzSequence.filter(num => num % 2 !== 0).sort((a, b) => a - b);
}
```
The function `getOddCollatz` first creates an array `collatzSequence` with the initial value of `n`. It then enters a while loop that continues until `current` is equal to 1. In each iteration of the loop, it checks if `current` is even or odd, and updates `current` accordingly. It also pushes the updated `current` into `collatzSequence`. Finally, it filters the `collatzSequence` to only include odd numbers, sorts them in increasing order, and returns the result.