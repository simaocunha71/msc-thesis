```js
const vowelsCount = (s) => {
  const vowelSet = new Set(['a', 'e', 'i', 'o', 'u']);
  let vowelCount = 0;
  for (let char of s.toLowerCase()) {
    if (vowelSet.has(char)) {
      vowelCount++;
    }
  }
  if (s.endsWith('y')) {
    vowelCount++;
  }
  return vowelCount;
}
```
