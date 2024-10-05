```js
const intersperse = (numbers, delimeter) => {
  return numbers.reduce((acc, cur, idx) => {
    if (idx !== 0) {
      acc.push(delimeter);
    }
    acc.push(cur);
    return acc;
  }, []);
};
```