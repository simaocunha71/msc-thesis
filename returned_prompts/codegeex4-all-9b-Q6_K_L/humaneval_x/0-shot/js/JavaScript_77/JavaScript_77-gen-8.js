```javascript
const iscube = (a) => {
  if (a < 0) a = -a;
  if (a === 0) return true;
  let i = 1;
  while (i * i * i <= a) {
    if (i * i * i === a) return true;
    i++;
  }
  return false;
}
```