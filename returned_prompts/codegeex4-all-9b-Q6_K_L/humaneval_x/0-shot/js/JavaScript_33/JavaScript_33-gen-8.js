```javascript
const sortThird = (l) => {
  let l1 = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 3 === 0) {
      l1.push(l[i]);
    }
  }
  l1.sort((a, b) => a - b);
  let k = 0;
  for (let i = 0; i < l.length; i++) {
    if (i % 3 === 0) {
      l[i] = l1[k];
      k++;
    }
  }
  return l;
};
```
