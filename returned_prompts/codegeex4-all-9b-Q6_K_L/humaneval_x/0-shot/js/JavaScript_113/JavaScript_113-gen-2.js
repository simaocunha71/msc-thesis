```js
const oddCount = (lst) => {
  return lst.map(str => {
    let count = 0;
    for (let c of str) {
      if (c % 2 !== 0) {
        count++;
      }
    }
    return `the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`;
  });
}
```
