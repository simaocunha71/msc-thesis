```js
const vowelsCount = (s) => {
  let v = 'aeiou';
  let y = s.endsWith('y');
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (v.includes(s[i].toLowerCase())) count++;
  }
  return count + y;
}
```