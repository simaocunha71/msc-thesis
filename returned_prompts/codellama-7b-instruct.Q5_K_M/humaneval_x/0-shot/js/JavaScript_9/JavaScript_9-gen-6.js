
```js
const rollingMax = numbers =>
  numbers.reduce(
    (acc, num, i) =>
      acc.concat(i === 0 ? num : Math.max(num, acc[i - 1])),
    []
  );

```