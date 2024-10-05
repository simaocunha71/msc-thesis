```javascript
const generateIntegers = (a, b) => {
  const isEven = (num) => num % 2 === 0;
  const getEvenDigits = (num) => String(num).split('').filter(isEven).map(Number);
  return [...new Set([...getEvenDigits(a), ...getEvenDigits(b)])].sort((a, b) => a - b);
}
```
