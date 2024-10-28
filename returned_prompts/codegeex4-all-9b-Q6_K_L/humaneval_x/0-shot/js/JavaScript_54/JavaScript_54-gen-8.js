```javascript
const sameChars = (s0, s1) => {
  if (s0.length !== s1.length) return false;
  let chars0 = s0.split('').sort().join('');
  let chars1 = s1.split('').sort().join('');
  return chars0 === chars1;
}
```