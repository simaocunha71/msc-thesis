```javascript
const sameChars = (s0, s1) => {
  let obj = {};
  for (let i = 0; i < s0.length; i++) {
    if (obj[s0[i]]) {
      obj[s0[i]]++;
    } else {
      obj[s0[i]] = 1;
    }
  }
  for (let j = 0; j < s1.length; j++) {
    if (obj[s1[j]]) {
      obj[s1[j]]--;
    } else {
      return false;
    }
  }
  for (let key in obj) {
    if (obj[key] !== 0) {
      return false;
    }
  }
  return true;
};
```
