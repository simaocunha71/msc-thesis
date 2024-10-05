```javascript
const concatenate = (strings) => strings.reduce((acc, current) => acc + current, '');
```
Explanation:

* The `concatenate` function takes an array of strings as an argument.
* The `reduce` method is used to concatenate the strings in the array. It takes two arguments: an accumulator (`acc`) and the current string (`current`).
* The initial value of the accumulator is an empty string (`''`).
* The callback function (`acc + current`) adds the current string to the accumulator.
* The `reduce` method returns the final concatenated string.

Example:
```javascript
console.log(concatenate(['a', 'b', 'c'])); // Output: "abc"
``` 