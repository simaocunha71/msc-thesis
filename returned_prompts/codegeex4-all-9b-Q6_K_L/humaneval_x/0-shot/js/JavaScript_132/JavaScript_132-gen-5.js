```javascript
  let nested = false;
  let open = 0;
  let close = 0;
  let openIndex = -1;
  let closeIndex = -1;
  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') {
      open++;
      openIndex = i;
    } else if (string[i] === ']') {
      close++;
      closeIndex = i;
    }
    if (open > 0 && close > 0 && openIndex < closeIndex) {
      nested = true;
      break;
    }
  }
  return nested;
}
```
