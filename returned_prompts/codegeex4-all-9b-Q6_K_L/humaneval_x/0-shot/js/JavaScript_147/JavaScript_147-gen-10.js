```javascript
const getMaxTriples = (n) => {
  const a = [];
  for (let i = 1; i <= n; i++) {
    a.push(i * i - i + 1);
  }
  let count = 0;
  for (let i = 0; i < n - 2; i++) {
    for (let j = i + 1; j < n - 1; j++) {
      for (let k = j + 1; k < n; k++) {
        if ((a[i] + a[j] + a[k]) % 3 === 0) {
          count++;
        }
      }
    }
  }
  return count;
}
```
