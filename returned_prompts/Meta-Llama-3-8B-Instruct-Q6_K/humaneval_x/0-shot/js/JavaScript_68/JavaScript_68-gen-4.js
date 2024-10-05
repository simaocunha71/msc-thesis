Here is a simple solution in JavaScript:
```
const pluck = (arr) => {
  if (arr.length === 0) return [];

  let minEvenValue = Infinity;
  let minEvenIndex = -1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < minEvenValue) {
      minEvenValue = arr[i];
      minEvenIndex = i;
    }
  }

  if (minEvenValue === Infinity) return [];

  return [minEvenValue, minEvenIndex];
};
```
Here's an explanation of the solution:

1. First, we check if the input array is empty. If it is, we return an empty array `[]`.
2. We initialize two variables: `minEvenValue` to keep track of the smallest even value, and `minEvenIndex` to keep track of the index of that value.
3. We iterate through the array using a `for` loop. For each node, we check if it's even (using the modulo operator `% 2 === 0`) and if it's smaller than the current `minEvenValue`. If both conditions are true, we update `minEvenValue` and `minEvenIndex`.
4. After the loop, we check if `minEvenValue` is still `Infinity`. If it is, it means there were no even values in the array, so we return an empty array `[]`.
5. Otherwise, we return an array containing the smallest even value and its index.

You can test this function with the examples provided in the problem statement to see that it produces the correct output.