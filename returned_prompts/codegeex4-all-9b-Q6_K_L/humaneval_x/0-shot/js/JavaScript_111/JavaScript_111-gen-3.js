```js
const histogram = (test) => {
  let words = test.split(' ');
  let count = {};
  let max = 0;
  let result = {};
  for (let i = 0; i < words.length; i++) {
    if (count[words[i]]) {
      count[words[i]] += 1;
    } else {
      count[words[i]] = 1;
    }
    if (count[words[i]] > max) {
      max = count[words[i]];
    }
  }
  for (let key in count) {
    if (count[key] === max) {
      result[key] = max;
    }
  }
  return result;
};
```
