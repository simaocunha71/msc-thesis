```
const incrList = (l) => l.map(x => x + 1);
```
Explanation:
The `incrList` function takes a list `l` as an argument. It uses the `map` method to create a new list where each element is incremented by 1. The `map` method applies a given function to each element of an array, returning a new array with the results.

For example, if we call `incrList([1, 2, 3])`, the function will return `[2, 3, 4]` because each element is incremented by 1. Similarly, if we call `incrList([5, 3, 5, 2, 3, 3, 9, 0, 123])`, the function will return `[6, 4, 6, 3, 4, 4, 10, 1, 124]`.