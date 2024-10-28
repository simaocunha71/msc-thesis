```js
const oddCount = (lst) => {
  return lst.map(
    (str) =>
      `the number of odd elements ${str
        .split('')
        .filter((ch) => parseInt(ch) % 2 !== 0).length}n the str${str
        .split('')
        .filter((ch) => parseInt(ch) % 2 !== 0).length}ng ${str
        .split('')
        .filter((ch) => parseInt(ch) % 2 !== 0).length} of the ${str
        .split('')
        .filter((ch) => parseInt(ch) % 2 !== 0).length}nput.`
  );
};
```