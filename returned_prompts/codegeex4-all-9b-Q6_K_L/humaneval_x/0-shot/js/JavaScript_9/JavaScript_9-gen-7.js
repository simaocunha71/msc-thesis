```js
const rollingMax = (numbers) => {
  return numbers.reduce((acc, num) => {
    if (num > acc[acc.length - 1]) {
      acc.push(num);
    } else {
      acc.push(acc[acc.length - 1]);
    }
    return acc;
  }, [numbers[0]]);
};
```
