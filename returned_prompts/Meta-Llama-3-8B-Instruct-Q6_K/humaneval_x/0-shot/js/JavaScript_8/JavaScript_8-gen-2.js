```javascript
const sumProduct = (numbers) => {
  if (numbers.length === 0) {
    return [0, 1];
  }
  let sum = 0;
  let product = 1;
  for (let num of numbers) {
    sum += num;
    product *= num;
  }
  return [sum, product];
};
``` 