Here is the solution in JavaScript:

```javascript
const evenOddCount = (num) => {
  let evenCount = 0;
  let oddCount = 0;

  for (let digit of num.toString().split('')) {
    if (+digit % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }

  return [evenCount, oddCount];
};
```

This function works by first initializing two counters, `evenCount` and `oddCount`, to 0. Then it iterates over each digit in the string representation of the input number using a `for...of` loop. For each digit, it checks whether the digit is even by using the modulo operator (`%`). If the remainder is 0, it means the digit is even, so it increments `evenCount`. Otherwise, it increments `oddCount`. Finally, it returns an array containing the counts of even and odd digits.