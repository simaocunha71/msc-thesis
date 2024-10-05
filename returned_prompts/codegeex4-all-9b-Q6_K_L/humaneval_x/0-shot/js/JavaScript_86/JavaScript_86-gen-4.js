```javascript
const antiShuffle = (s) => {
  if (s.length === 0) return '';
  const words = s.split(' ');
  return words.map(word => word.split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('')).join(' ');
}
```
