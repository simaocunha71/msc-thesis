```javascript
const specialFilter = (nums) => {
  let count = 0;
  for (let num of nums) {
    if (num > 10 && num % 2 !== 0) {
      let firstDigit = Math.abs(num) % 10;
      let lastDigit = Math.floor(Math.abs(num) / 10) % 10;
      if (firstDigit % 2 !== 0 && lastDigit % 2 !== 0) {
        count++;
      }
    }
  }
  return count;
}
```