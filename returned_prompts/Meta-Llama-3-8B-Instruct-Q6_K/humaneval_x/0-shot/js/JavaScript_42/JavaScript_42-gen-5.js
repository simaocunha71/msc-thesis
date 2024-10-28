```javascript
const incrList = (l) => l.map(x => x + 1);
```
Explanation:
The problem is asking to create a function `incrList` that takes a list `l` as input and returns a new list where each element is incremented by 1.

The solution uses the `map` method of the array, which applies a given function to each element of the array and returns a new array with the results. In this case, the function is a simple lambda function `x => x + 1` that increments each element by 1.

For example, if the input list is `[1, 2, 3]`, the function will return `[2, 3, 4]`. If the input list is `[5, 3, 5, 2, 3, 3, 9, 0, 123]`, the function will return `[6, 4, 6, 3, 4, 4, 10, 1, 124]`.