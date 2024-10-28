```js
const sortEven = (l) => {
  var evens = l.filter((item, index) => index % 2 === 0).sort((a, b) => a - b);
  var result = l.map((item, index) => {
    if (index % 2 === 0) {
      return evens.shift();
    } else {
      return item;
    }
  });
  return result;
}
```