```js
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    let countA = a.toString(2).split('1').length - 1;
    let countB = b.toString(2).split('1').length - 1;
    if (countA === countB) return a - b;
    return countA - countB;
  });
}
```
