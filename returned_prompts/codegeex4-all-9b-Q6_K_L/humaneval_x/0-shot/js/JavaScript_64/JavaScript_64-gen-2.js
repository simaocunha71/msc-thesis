```js
const vowelsCount = (s) => {
  const vowels = 'aeiou';
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i])) {
      count++;
    }
  }
  if (s[s.length - 1] === 'y') {
    count++;
  }
  return count;
}
```