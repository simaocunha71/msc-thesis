```javascript
const oddCount = (lst) => {
  return lst.map(e => {
    let count = 0;
    for (let i = 0; i < e.length; i++) {
      if (parseInt(e[i]) % 2 !== 0) {
        count++;
      }
    }
    return `the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`;
  });
};
```