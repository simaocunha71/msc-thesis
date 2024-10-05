```js
const sortThird = (l) => {
  let l1 = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 3 === 0) {
      l1.push(l[i]);
    }
  }
  l1.sort((a, b) => a - b);
  let l2 = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 3 === 0) {
      l2.push(l1.shift());
    } else {
      l2.push(l[i]);
    }
  }
  return l2;
}
```