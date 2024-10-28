```javascript
  let result = 2;
  while (n > 2) {
    if (n % result === 0) {
      n /= result;
    } else {
      result++;
    }
  }
  return result;
}
```