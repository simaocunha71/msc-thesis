```js
const sortEven = (l) => {
  const evens = l.filter((_, i) => i % 2 === 0).sort((a, b) => a - b);
  const result = [];
  let evenIndex = 0;
  for (let i = 0; i < l.length; i++) {
    if (i % 2 === 0) {
      result[i] = evens[evenIndex++];
    } else {
      result[i] = l[i];
    }
  }
  return result;
}
```