Here's how you could do it:

```javascript
const triplesSumToZero = (l) => {
  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      for (let k = j + 1; k < l.length; k++) {
        if (l[i] + l[j] + l[k] === 0) {
          return true;
        }
      }
    }
  }
  return false;
}
```

This function uses three nested loops to check every combination of three distinct elements in the list. If it finds three elements that sum to zero, it returns true. If it goes through the entire list without finding such a combination, it returns false.