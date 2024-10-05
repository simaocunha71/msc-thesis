You can solve this problem using JavaScript's built-in `every` method. This method tests whether all elements in the array pass the test implemented by the provided function. Here's how you can do it:

```javascript
const belowThreshold = (l, t) => {
  return l.every(num => num < t);
}
```

The `every` method will iterate through each number in the array `l` and check if it is less than `t`. If all numbers pass the test, it will return `true`. If any number fails the test, it will return `false`.

Please note that this code assumes that the input `l` is an array of numbers and `t` is a number. If these assumptions are not met, the code may produce unexpected results.