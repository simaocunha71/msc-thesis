  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  const range = max - min;

  return numbers.map(n => (n - min) / range);
};

console.log(rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0]));  // [0, 0.25, 0.5, 0.75, 1]

```

## Output

```
[ 0, 0.25, 0.5, 0.75, 1 ]
```

## Explanation

The function rescaleToUnit takes an array of numbers as input. It first calculates the minimum and maximum values of the array using the Math.min and Math.max functions. Then, it calculates the range of the values (max - min). After that, it maps over the array and for each number, it subtracts the minimum value from the number and divides the result by the range. This linear transformation scales the numbers such that the smallest number becomes 0 and the largest number becomes 1.

Finally, it returns the transformed array.

The result of the function call `rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])` is `[0, 0.25, 0.5, 0.75, 1]` which is the expected output.

## Complexity

The time complexity of this function is O(n) because it needs to iterate over the array of numbers once to calculate the minimum and maximum values, and then again to map over the array and apply the transformation. The space complexity is O(n) because of the space required to store the transformed array.

## Constraints

The input array must have at least two elements, as described in the problem statement.

## Test Cases

- `rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])` should return `[0, 0.25, 0.5, 0.75, 1]`
-