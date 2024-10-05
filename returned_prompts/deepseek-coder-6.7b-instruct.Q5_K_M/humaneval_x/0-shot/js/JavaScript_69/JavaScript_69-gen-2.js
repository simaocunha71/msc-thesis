  let count = {};

  // Count the frequency of each number in the list.
  for (let num of lst) {
    if (count[num]) {
      count[num]++;
    } else {
      count[num] = 1;
    }
  }

  // Start from the maximum number in the list and go down.
  for (let i = Math.max(...lst); i > 0; i--) {
    if (count[i]) {
      // Return the first number that has a frequency >= to its value.
      if (count[i] >= i) {
        return i;
      }
    }
  }

  // If no such a value exist, return -1.
  return -1;
}
```

```javascript
console.log(search([4, 1, 2, 2, 3, 1])) // 2
console.log(search([1, 2, 2, 3, 3,