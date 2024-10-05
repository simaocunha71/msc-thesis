```
  return strings.filter(s => s.startsWith(prefix));
```


This function takes an array of strings (`strings`) and a prefix (`prefix`) as input. It uses the `filter()` method to create a new array with only the strings that start with the given prefix. The `startsWith()` method is used to check if a string starts with the given prefix.

For example, if the input array is `['abc', 'bcd', 'cde', 'array']` and the prefix is `'a'`, the function will return `['abc', 'array']`, as these are the strings that start with the prefix `'a'`. If the input array is `[]` and the prefix is `'a'`, the function will return an empty array, as there are no strings that start with the prefix `'a'`.