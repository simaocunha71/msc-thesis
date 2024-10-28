```js
const sameChars = (s0, s1) => {
  let s0Set = new Set(s0);
  let s1Set = new Set(s1);
  if (s0Set.size !== s1Set.size) {
    return false;
  }
  for (let char of s0Set) {
    if (!s1Set.has(char)) {
      return false;
    }
  }
  return true;
}
```