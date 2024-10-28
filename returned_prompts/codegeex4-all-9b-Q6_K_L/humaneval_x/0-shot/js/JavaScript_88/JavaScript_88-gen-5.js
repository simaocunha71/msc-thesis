```javascript
  const first = array[0];
  const last = array[array.length - 1];
  const sum = first + last;
  return sum % 2 === 0 ? array.sort((a, b) => b - a) : array.sort((a, b) => a - b);
}
```