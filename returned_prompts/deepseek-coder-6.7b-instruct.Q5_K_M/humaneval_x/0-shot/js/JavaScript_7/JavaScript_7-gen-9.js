  return strings.filter(string => string.includes(substring));
};

console.log(filterBySubstring([], 'a')); // []
console.log(filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')); // ['abc', 'bacd', 'array']

```

## 1.11

```js
