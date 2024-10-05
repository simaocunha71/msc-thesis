```js
const antiShuffle = (s) => {
  return s
    .split(' ')
    .map((word) => {
      if (word.length === 1) return word;
      let letters = word.split('');
      letters.sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0));
      return letters.join('');
    })
    .join(' ');
};
```
