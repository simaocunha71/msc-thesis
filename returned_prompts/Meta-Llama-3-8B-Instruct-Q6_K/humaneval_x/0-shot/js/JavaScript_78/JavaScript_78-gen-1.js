```javascript
const hexKey = (num) => {
  let count = 0;
  for (let i = 0; i < num.length; i++) {
    const digit = num[i];
    switch (digit) {
      case 'B':
      case 'D':
      case 'F':
      case '7':
        count++;
        break;
      case '2':
      case '3':
      case '5':
      case 'A': // A is decimal 10, which is also a prime
        count++;
        break;
    }
  }
  return count;
};
```