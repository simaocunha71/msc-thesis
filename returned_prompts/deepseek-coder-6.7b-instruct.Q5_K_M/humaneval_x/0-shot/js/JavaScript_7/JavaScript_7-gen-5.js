  return strings.filter(str => str.includes(substring))

};

console.log(filterBySubstring([], 'a')); // []
console.log(filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')); // ['abc', 'bacd', 'array']
```

## Exercise 3

```js
