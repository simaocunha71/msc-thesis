  return strings.filter(string => string.includes(substring));

};

console.log(filterBySubstring([], 'a')); // []
console.log(filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')); // ['abc', 'bacd', 'array']

// filterBySubstring is a function that takes in an array of strings and a substring. 
// It uses the array filter method to filter out the strings that don't contain the substring. 
// It uses the string includes method to check if the string contains the substring.
```

## Exercise 3

```javascript
