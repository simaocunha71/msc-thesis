```js
const oddCount = (lst) => {
  let result = [];
  for (let i = 0; i < lst.length; i++) {
    let count = 0;
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] % 2 !== 0) {
        count++;
      }
    }
    result.push(`the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`);
  }
  return result;
}
```