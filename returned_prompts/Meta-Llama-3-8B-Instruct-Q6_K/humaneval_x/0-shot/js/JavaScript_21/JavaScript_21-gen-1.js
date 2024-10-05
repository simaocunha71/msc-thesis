Here is the solution in JavaScript:
```
const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map((n) => (n - min) / (max - min));
};
```


Explanation:
1. We use the `Math.min` and `Math.max` functions to find the smallest and largest numbers in the list respectively.
2. We then use the `map` method to apply a transformation to each number in the list.
3. The transformation is `(n - min) / (max - min)`, which scales each number to the range [0, 1]. The smallest number becomes 0, and the largest becomes 1. All other numbers are scaled proportionally.
4. The `map` method returns a new array with the transformed numbers.

For example, if we call `rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])`, the output will be `[0.0, 0.25, 0.5, 0.75, 1.0]`.