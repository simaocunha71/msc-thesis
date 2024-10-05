```js
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    const aOnes = a.toString(2).split('1').length - 1;
    const bOnes = b.toString(2).split('1').length - 1;
    return aOnes - bOnes || a - b;
  });
}
```
