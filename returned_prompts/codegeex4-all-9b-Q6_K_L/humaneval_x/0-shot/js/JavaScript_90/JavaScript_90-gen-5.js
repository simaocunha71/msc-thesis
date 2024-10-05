```javascript
  let sorted = lst.sort((a, b) => a - b);
  let smallest = sorted[0];
  for (let i = 0; i < sorted.length; i++) {
    if (sorted[i] > smallest) {
      return sorted[i];
    }
  }
  return null;
}
```
