```javascript
const incrList = (l) => l.map(x => x + 1);
```
Explanation:
The problem is asking to create a function that takes a list of numbers as an input and returns a new list where each element is incremented by 1.

The solution uses the built-in `map` method in JavaScript, which applies a function to each element of an array and returns a new array with the results. In this case, the function is a simple addition of 1 to each element (`x + 1`).

For example, if we call `incrList([1, 2, 3])`, the function will return `[2, 3, 4]`, which is the original list with each element incremented by 1. Similarly, if we call `incrList([5, 3, 5, 2, 3, 3, 9, 0, 123])`, the function will return `[6, 4, 6, 3, 4, 4, 10, 1, 124]`, which is the original list with each element incremented by 1.