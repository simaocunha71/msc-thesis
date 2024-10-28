```javascript
const fixSpaces = (text) => {
  text = text.replace(/\s+/g, ' ');
  let arr = text.split(' ');
  if (arr.length > 2) {
    for (let i = 2; i < arr.length; i++) {
      if (arr[i] === '' && arr[i-1] === '' && arr[i-2] === '') {
        arr[i] = '-';
        arr[i-1] = '';
        arr[i-2] = '';
      }
    }
  }
  return arr.join('_');
}
```
