return strings.filter(str => str.includes(substring))
}

console.log(filterBySubstring([], 'a')) // []
console.log(filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')) // ['abc', 'bacd', 'array']
```

## Exercise 2:

Write a function `countBySubstring` that counts how many times a given substring appears in an array of strings.

```javascript
