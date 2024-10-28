```javascript
const f = (n) => {
  const isEven = (num) => num % 2 === 0;
  const factorial = (num) => num > 0 ? num * factorial(num - 1) : 1;
  const sum = (num) => num > 0 ? num + sum(num - 1) : 0;

  return Array.from({length: n}, (_, i) => isEven(i + 1) ? factorial(i + 1) : sum(i + 1));
}
```