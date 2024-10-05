```javascript
const countUpper = (s) => {
  const vowels = ['A', 'E', 'I', 'O', 'U'];
  let count = 0;
  for (let i = 0; i < s.length; i += 2) {
    if (vowels.includes(s[i])) {
      count++;
    }
  }
  return count;
}
```