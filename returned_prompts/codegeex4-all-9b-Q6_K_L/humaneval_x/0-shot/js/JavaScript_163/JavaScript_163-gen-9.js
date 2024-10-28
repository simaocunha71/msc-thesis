```js
const generateIntegers = (a, b) => {
  let start = a;
  let end = b;
  let result = [];
  
  if (a > b) {
    start = b;
    end = a;
  }
  
  for (let i = start; i <= end; i++) {
    let num = i;
    while (num > 0) {
      let digit = num % 10;
      if (digit % 2 === 0) {
        result.push(digit);
      }
      num = Math.floor(num / 10);
    }
  }
  
  return result;
};
```