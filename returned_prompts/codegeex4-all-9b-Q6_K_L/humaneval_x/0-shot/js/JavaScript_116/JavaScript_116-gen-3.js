```js
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    let a_ones = a.toString(2).split('').filter(x => x == 1).length;
    let b_ones = b.toString(2).split('').filter(x => x == 1).length;
    if (a_ones == b_ones) {
      return a - b;
    } else {
      return a_ones - b_ones;
    }
  });
}
```
