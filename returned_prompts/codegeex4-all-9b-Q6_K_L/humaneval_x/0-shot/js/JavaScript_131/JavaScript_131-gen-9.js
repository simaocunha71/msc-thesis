```js
const digits = (n) => {
  let str = n.toString();
  let product = 1;
  let isEven = true;
  for (let i = 0; i < str.length; i++) {
    if (parseInt(str[i]) % 2 !== 0) {
      product *= parseInt(str[i]);
      isEven = false;
    }
  }
  return isEven ? 0 : product;
}
```
