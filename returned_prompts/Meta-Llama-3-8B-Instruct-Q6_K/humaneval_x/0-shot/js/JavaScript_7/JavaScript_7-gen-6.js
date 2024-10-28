Here is a possible solution using the `filter()` method and a callback function:
```
const filterBySubstring = (strings, substring) => strings.filter(str => str.includes(substring));
```
Here's an explanation of how the code works:

* The `filter()` method is called on the `strings` array, which returns a new array with only the elements that pass the test implemented by the provided callback function.
* The callback function `str => str.includes(substring)` takes a string `str` as an argument and returns a boolean indicating whether the string contains the `substring`.
* The `includes()` method checks if the string contains the `substring` and returns `true` if it does, and `false` otherwise.
* The `filter()` method returns a new array containing only the strings that return `true` when passed to the callback function, i.e., the strings that contain the `substring`.

You can test the function with the examples you provided:
```
console.log(filterBySubstring([], 'a')); // []
console.log(filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')); // ['abc', 'bacd', 'array']
```
I hope this helps! Let me know if you have any questions. 😊

---

Note: The `includes()` method is a case-sensitive search. If you want to perform a case-insensitive search, you can use the `toLowerCase()` method to convert both the string and the substring to lowercase before comparing them. For example:
```
const filterBySubstring = (strings, substring) => strings.filter(str => str.toLowerCase().includes(substring.toLowerCase()));
```
This way, the search will be case-insensitive. 🎉