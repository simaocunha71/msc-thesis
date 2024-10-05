```js
const generateIntegers = (a, b) => {
  if (a > b) {
    return generateIntegers(b, a);
  }
  const evenDigits = [];
  for (let i = a; i <= b; i++) {
    const digits = Array.from(String(i), Number);
    for (let j = 0; j < digits.length; j++) {
      if (digits[j] % 2 === 0) {
        evenDigits.push(digits[j]);
        break;
      }
    }
  }
  return evenDigits;
};
```