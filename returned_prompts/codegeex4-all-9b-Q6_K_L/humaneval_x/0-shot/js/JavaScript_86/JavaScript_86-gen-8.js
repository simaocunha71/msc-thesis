```javascript
const antiShuffle = (s) => {
  let words = s.split(' ');
  for (let i = 0; i < words.length; i++) {
    words[i] = words[i].split('').sort().join('');
  }
  return words.join(' ');
}
```
