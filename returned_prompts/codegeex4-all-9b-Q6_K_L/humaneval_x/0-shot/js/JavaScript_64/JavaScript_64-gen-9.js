```js
const vowelsCount = (s) => {
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i].toLowerCase())) {
      count++;
    }
  }
  if (s[s.length - 1].toLowerCase() === 'y') {
    count++;
  }
  return count;
}
```
