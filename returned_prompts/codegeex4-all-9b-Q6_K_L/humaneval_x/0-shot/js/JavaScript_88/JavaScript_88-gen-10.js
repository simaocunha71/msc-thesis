```js
  let res = [...array].sort((a, b) => a - b);
  let sum = array[0] + array[array.length - 1];
  return sum % 2 === 0 ? res.reverse() : res;
}
```