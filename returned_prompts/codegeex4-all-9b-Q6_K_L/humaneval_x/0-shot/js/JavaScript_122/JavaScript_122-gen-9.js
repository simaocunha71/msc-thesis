```js
const addElements = (arr, k) => {
  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (String(arr[i]).length <= 2) {
      sum += arr[i];
    }
  }
  return sum;
};
```