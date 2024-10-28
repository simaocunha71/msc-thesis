```
const sumSquares = (lst) => {
  return lst.map(Math.ceil).map(x => x ** 2).reduce((acc, curr) => acc + curr, 0);
};
```


Explanation:
The function `sumSquares` takes a list of numbers as input. It uses the `map` function to apply two operations to each element in the list:
- First, it uses `Math.ceil` to round each element to the upper int(Ceiling).
- Then, it squares each element using the exponentiation operator `** 2`.

After the list is processed, it uses the `reduce` function to calculate the sum of the squared numbers. The initial value of the accumulator `acc` is set to 0, and the function adds each squared number to the accumulator. The final result is the sum of the squared numbers.