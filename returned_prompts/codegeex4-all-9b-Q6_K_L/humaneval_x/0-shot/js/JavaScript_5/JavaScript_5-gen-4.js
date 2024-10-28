```js
const intersperse = (numbers, delimeter) => {
  return numbers.reduce((acc, num, i) => {
    if (i !== 0) {
      acc.push(delimeter);
    }
    acc.push(num);
    return acc;
  }, []);
};
```