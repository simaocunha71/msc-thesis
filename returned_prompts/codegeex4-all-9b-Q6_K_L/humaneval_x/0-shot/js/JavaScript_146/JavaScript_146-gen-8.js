```js
const specialFilter = (nums) => {
  let count = 0;
  for (let num of nums) {
    if (num > 10 && num % 2 !== 0) {
      let firstDigit = parseInt(num.toString()[0]);
      let lastDigit = parseInt(num.toString()[num.toString().length - 1]);
      if (firstDigit % 2 !== 0 && lastDigit % 2 !== 0) {
        count++;
      }
    }
  }
  return count;
};
```
