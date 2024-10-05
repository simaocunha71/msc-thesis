```js
const canArrange = (arr) => {
  let maxInd = -1;
  for (let i = 1; i < arr.length; ++i) {
    if (arr[i] < arr[i - 1]) {
      maxInd = i - 1;
    }
  }
  return maxInd;
}
```