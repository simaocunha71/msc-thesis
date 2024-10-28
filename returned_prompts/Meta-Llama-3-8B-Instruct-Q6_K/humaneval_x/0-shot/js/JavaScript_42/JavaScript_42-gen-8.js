```
const incrList = (l) => l.map(x => x + 1);
```


Explanation:
The task is to create a function `incrList` that takes a list of numbers as input and returns a new list where each element is incremented by 1.

We can use the built-in `map` function in JavaScript to achieve this. The `map` function applies a transformation to each element of an array and returns a new array with the results.

In this case, we define a function that takes a list `l` as input. We then use the `map` function to apply a transformation to each element of the list. The transformation is a function that takes an element `x` and returns `x + 1`.

This effectively increments each element of the list by 1, and the resulting list is returned. The `map` function returns a new array with the transformed elements, so we don't need to worry about modifying the original list.

For example, if we call `incrList([1, 2, 3])`, the function will return `[2, 3, 4]`. If we call `incrList([5, 3, 5, 2, 3, 3, 9, 0, 123])`, the function will return `[6, 4, 6, 3, 4, 4, 10, 1, 124]`.