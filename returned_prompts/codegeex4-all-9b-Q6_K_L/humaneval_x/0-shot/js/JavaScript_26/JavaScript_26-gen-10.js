```javascript
  const duplicates = new Set();
  const result = [];
  for (let i = 0; i < numbers.length; i++) {
    if (!duplicates.has(numbers[i])) {
      result.push(numbers[i]);
      duplicates.add(numbers[i]);
    }
  }
  return result;
};
```