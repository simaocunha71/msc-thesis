```javascript
const fizzBuzz = (n) => {
  const isDivisibleBy11Or13 = (num) => num % 11 === 0 || num % 13 === 0;
  const countSevens = (num) => num.toString().split('').filter(x => x === '7').length;
  let count = 0;
  for (let i = 1; i < n; i++) {
    if (isDivisibleBy11Or13(i)) {
      count += countSevens(i);
    }
  }
  return count;
}
```