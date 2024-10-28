```js
  return string
    .split('')
    .map(char => char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase())
    .join('');
};
```

