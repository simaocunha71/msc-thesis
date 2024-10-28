```js
const generateIntegers = (a, b) => {
  const evenDigits = [2, 4, 6, 8];
  let result = [];
  
  for (let i = a; i <= b; i++) {
    let num = i;
    while (num > 0) {
      let digit = num % 10;
      if (evenDigits.includes(digit)) {
        result.push(i);
        break;
      }
      num = Math.floor(num / 10);
    }
  }
  
  return result;
};
```