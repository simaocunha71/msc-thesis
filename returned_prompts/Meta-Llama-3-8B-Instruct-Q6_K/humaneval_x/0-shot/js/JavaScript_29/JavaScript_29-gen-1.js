Here is a possible implementation of the `filterByPrefix` function in JavaScript:
```
const filterByPrefix = (strings, prefix) => strings.filter(str => str.startsWith(prefix));
```
This implementation uses the `filter` method to create a new array containing only the elements of the original array that pass the test implemented by the provided function. The test is implemented by the `startsWith` method, which checks whether the string starts with the given prefix.

You can test this implementation using the examples you provided:
```
console.log(filterByPrefix([], 'a')); // []
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')); // ['abc', 'array']
```
This implementation is concise and efficient, as it uses built-in methods to perform the filtering. It also has the desired behavior of returning an empty array if the input list is empty, and returning only the strings that start with the given prefix.