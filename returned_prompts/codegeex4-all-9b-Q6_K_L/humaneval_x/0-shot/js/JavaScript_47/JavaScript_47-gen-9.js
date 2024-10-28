```js
const median = (l) => {
  const sortedL = l.sort((a, b) => a - b);
  const midIndex = Math.floor(sortedL.length / 2);

  if (sortedL.length % 2 === 0) {
    return (sortedL[midIndex - 1] + sortedL[midIndex]) / 2;
  } else {
    return sortedL[midIndex];
  }
}
```