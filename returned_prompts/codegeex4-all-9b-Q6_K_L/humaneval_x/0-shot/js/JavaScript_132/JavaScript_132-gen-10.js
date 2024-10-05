```js
  let opening = [];
  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') {
      opening.push(i);
    } else {
      if (opening.length > 0) {
        opening.pop();
        if (opening.length > 0) {
          return true;
        }
      }
    }
  }
  return false;
}
```