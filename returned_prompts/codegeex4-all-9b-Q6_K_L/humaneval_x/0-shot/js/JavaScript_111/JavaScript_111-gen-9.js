```js
const histogram = (test) => {
  let str = test.split(' ');
  let obj = {};

  for (let i = 0; i < str.length; i++) {
    if (obj[str[i]]) {
      obj[str[i]]++;
    } else {
      obj[str[i]] = 1;
    }
  }

  let max = 0;
  for (let key in obj) {
    if (obj[key] > max) {
      max = obj[key];
    }
  }

  let result = {};
  for (let key in obj) {
    if (obj[key] === max) {
      result[key] = max;
    }
  }

  return result;
};
```