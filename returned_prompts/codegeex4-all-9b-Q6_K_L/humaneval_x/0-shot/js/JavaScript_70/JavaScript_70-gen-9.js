```js
const strangeSortList = (lst) => {
  let arr = [];
  let min = Math.min(...lst);
  let max = Math.max(...lst);

  while (lst.length > 0) {
    if (lst.includes(min)) {
      arr.push(min);
      lst.splice(lst.indexOf(min), 1);
    } else {
      arr.push(max);
      lst.splice(lst.indexOf(max), 1);
    }
  }
  return arr;
}
```
