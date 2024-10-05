```js
  const counts = {};
  test.split(' ').forEach((letter) => {
    if (counts[letter]) {
      counts[letter]++;
    } else {
      counts[letter] = 1;
    }
  });
  const maxCount = Math.max(...Object.values(counts));
  return Object.keys(counts).reduce((result, key) => {
    if (counts[key] === maxCount) {
      result[key] = maxCount;
    }
    return result;
  }, {});
};
```

B:
```js
  const counts = {};
  test.split(' ').forEach((letter) => {
    if (counts[letter]) {
      counts[letter]++;
    } else {
      counts[letter] = 1;
    }
  });
  const maxCount = Math.max(...Object.values(counts));
  return Object.keys(counts).reduce((result, key) => {
    if (counts[key] === maxCount) {
      result.push({ [key]: maxCount });
    }
    return result;
  }, []);
};
```