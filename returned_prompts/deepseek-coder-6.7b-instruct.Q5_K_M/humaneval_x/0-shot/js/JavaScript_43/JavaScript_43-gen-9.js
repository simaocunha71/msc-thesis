  const set = new Set();
  for (let num of l) {
    if (set.has(-num)) {
      return true;
    }
    set.add(num);
  }
  return false;
}

module.exports = pairsSumToZero;
```

## Solution 2

```javascript
