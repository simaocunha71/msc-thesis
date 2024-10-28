```js
const sortEven = (l) => {
  var evens = [];
  for (let i = 0; i < l.length; i += 2) {
    evens.push(l[i]);
  }
  evens.sort((a, b) => a - b);
  for (let i = 0; i < evens.length; i++) {
    l[i * 2] = evens[i];
  }
  return l;
}
```