```javascript
const strlen = (string) => {
  if (typeof string !== 'string') {
    throw new TypeError('Argument must be a string');
  }
  return string.length;
}
```