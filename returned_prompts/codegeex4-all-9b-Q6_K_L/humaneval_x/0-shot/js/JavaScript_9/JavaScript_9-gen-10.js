```js
const rollingMax = (numbers) => {
  return numbers.reduce((acc, n) => {
    acc.push(Math.max(...acc, n));
    return acc;
  }, []);
}
```