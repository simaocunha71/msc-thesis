```js
const uniqueDigits = (x) => {
  return x.filter(num => {
    let str = num.toString();
    for (let i = 0; i < str.length; i++) {
      if (parseInt(str[i]) % 2 === 0) {
        return false;
      }
    }
    return true;
  }).sort((a, b) => a - b);
}
```
