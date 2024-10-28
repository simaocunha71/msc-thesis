You can solve this problem by using the `reduce` method of an array. 

Here is the solution:

```javascript
const concatenate = (strings) => {
    return strings.reduce((acc, curr) => acc + curr, '');
};
```

The `reduce` method takes two parameters: a callback function and an initial value. The callback function itself takes two parameters: an accumulator and the current value. In this case, the accumulator (`acc`) is the string that is being built up, and the current value (`curr`) is the current string in the array. 

The callback function returns the concatenation of the accumulator and the current value. The initial value is an empty string (`''`), which means that the first string in the array will be added to the accumulator. 

Finally, the `reduce` method returns the final value of the accumulator, which is the concatenated string.