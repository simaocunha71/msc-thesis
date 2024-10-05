  if (arr.length === 0) return null;

  let sum = 0;
  let prod = 1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
      prod *= -1;
      sum += Math.abs(arr[i]);
    } else if (arr[i] > 0) {
      prod *= 1;
      sum += arr[i];
    } else {
      return 0;
    }
  }

  return prod * sum;
};

console.log(prodSigns([1, 2, 2, -4])); // -9
console.log(prodSigns([0, 1])); // 0
console.log(prodSigns([])); // null

module.exports = prodSigns;
```

## 13. Code: Find the median of a list of numbers
```javascript
