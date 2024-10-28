```js
const largestSmallestIntegers = (lst) => {
  let a = null;
  let b = null;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0) {
      if (a === null || lst[i] > a) {
        a = lst[i];
      }
    } else if (lst[i] > 0) {
      if (b === null || lst[i] < b) {
        b = lst[i];
      }
    }
  }
  return [a, b];
}
```