```js
const addElements = (arr, k) => {
  return arr.slice(0, k).reduce((sum, num) => {
    const digits = num.toString().length;
    if (digits <= 2) {
      return sum + num;
    }
    return sum;
  }, 0);
};
```