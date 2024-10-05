```javascript
const iscube = (a) => {
  let i = 0;
  while (i*i*i <= a) {
    if (i*i*i === a) {
      return true;
    }
    i++;
  }
  return false;
}
```
