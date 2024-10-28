```javascript
const addElements = (arr, k) => {
  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (arr[i] < 10) {
      sum += arr[i];
    } else if (arr[i] < 100) {
      sum += arr[i];
    }
  }
  return sum;
};
```