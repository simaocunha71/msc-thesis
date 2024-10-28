```
const incrList = (l) => l.map(x => x + 1);
```


Explanation:
The problem is asking to create a function called `incrList` that takes a list of numbers as an argument and returns a new list where each element is incremented by 1.

The solution uses the `map` method, which is a built-in method in JavaScript that applies a function to every element in an array. In this case, the function is a simple addition of 1 to each element. The `map` method returns a new array with the results, so we don't need to modify the original list.

For example, if we call `incrList([1, 2, 3])`, the function will return `[2, 3, 4]`, which is the original list with each element incremented by 1. If we call `incrList([5, 3, 5, 2, 3, 3, 9, 0, 123])`, the function will return `[6, 4, 6, 3, 4, 4, 10, 1, 124]`, which is the original list with each element incremented by 1.