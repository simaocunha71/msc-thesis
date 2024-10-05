  return strings.filter(string => string.includes(substring));
}

console.log(filterBySubstring(["abc", "bacd", "cde", "array"], "a")); // ['abc', 'bacd', 'array']
console.log(filterBySubstring([], "a")); // []
```

## 2. Filtering Objects

```js
