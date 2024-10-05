```js
  const mapping = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  };
  const roman = [];
  let temp = 0;
  for (let i = 1000; i > 0; i /= 10) {
    temp = Math.floor(number / i);
    if (temp === 4) {
      roman.push(mapping[i] + mapping[i * 5]);
    } else if (temp === 9) {
      roman.push(mapping[i] + mapping[i * 10]);
    } else if (temp < 4) {
      for (let j = 0; j < temp; j++) {
        roman.push(mapping[i]);
      }
    } else {
      roman.push(mapping[i * 5]);
      for (let j = 0; j < temp - 5; j++) {
        roman.push(mapping[i]);
      }
    }
    number %= i;
  }
  return roman.join('');
};
```
