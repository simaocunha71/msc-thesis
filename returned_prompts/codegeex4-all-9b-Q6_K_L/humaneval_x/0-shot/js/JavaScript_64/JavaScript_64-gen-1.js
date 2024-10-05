```js
const vowelsCount = (s) => {
  let count = 0;
  const vowels = 'aeiou';
  for (let i = 0; i < s.length; i++) {
    if (vowels.indexOf(s[i].toLowerCase()) !== -1) {
      count++;
    }
  }
  return count;
}
```