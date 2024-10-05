```
const filterByPrefix = (strings, prefix) => strings.filter(str => str.startsWith(prefix));
```


Explanation:
This problem requires creating a function that filters a list of strings based on a given prefix. The function should return a new list containing only the strings that start with the given prefix.

The solution uses the built-in `filter()` method of JavaScript arrays, which creates a new array with all the elements that pass the test implemented by the provided function.

The function `filterByPrefix` takes two parameters: `strings` (the list of strings to filter) and `prefix` (the prefix to filter by). It uses the `startsWith()` method to check if each string in the `strings` list starts with the given `prefix`. If a string starts with the prefix, it is included in the new list; otherwise, it is excluded.

For example, if we call `filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')`, the function will return `['abc', 'array']`, which are the strings that start with the prefix 'a'. If we call `filterByPrefix([], 'a')`, the function will return an empty list, since there are no strings that start with the prefix 'a'.