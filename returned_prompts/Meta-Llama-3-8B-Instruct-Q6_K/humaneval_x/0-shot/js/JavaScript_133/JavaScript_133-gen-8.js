```
const sumSquares = (lst) => {
  return Math.round(lst.map(x => Math.ceil(x)).map(x => x ** 2)).reduce((a, b) => a + b, 0);
};
```


The function `sumSquares` takes a list `lst` as an argument. It uses the `map` method to apply the following operations to each element in the list:

1. `Math.ceil(x)`: This rounds each element up to its ceiling.
2. `x ** 2`: This squares each element.

The `map` method returns a new array with the results of these operations. The `reduce` method is then used to sum up these squared and rounded numbers.

For example, if `lst` is `[1, 2, 3]`, the `map` method will return `[(Math.ceil(1)), (Math.ceil(2)), (Math.ceil(3))] = [2, 3, 4]`. Then, the `map` method will return `[(2 ** 2), (3 ** 2), (4 ** 2)] = [4, 9, 16]`. Finally, the `reduce` method will sum up these numbers, returning `4 + 9 + 16 = 29`.