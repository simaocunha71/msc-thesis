```javascript
const digits = (n) => {
  let str = n.toString();
  let product = 1;
  let hasOdd = false;
  for (let i = 0; i < str.length; i++) {
    if (parseInt(str[i]) % 2 !== 0) {
      product *= parseInt(str[i]);
      hasOdd = true;
    }
  }
  return hasOdd ? product : 0;
}
```
