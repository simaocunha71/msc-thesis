```javascript
  let res = 0;
  let count = 9;
  for (let i = 1; i < n; i++) {
    res += count;
    count *= 9;
  }
  return res * 2 + 1;
};
```