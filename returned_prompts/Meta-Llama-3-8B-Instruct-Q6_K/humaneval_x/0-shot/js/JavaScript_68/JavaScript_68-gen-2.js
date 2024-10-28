Here is a JavaScript function that solves the problem:
```
const pluck = (arr) => {
  if (arr.length === 0) return [];

  const evenNodes = arr.filter(node => node % 2 === 0);
  if (evenNodes.length === 0) return [];

  const smallestEvenValue = Math.min(...evenNodes);
  const smallestEvenIndex = arr.indexOf(smallestEvenValue);

  return [smallestEvenValue, smallestEvenIndex];
};
```
Here's an explanation of the code:

1. We first check if the input array is empty. If it is, we return an empty array.
2. We use the `filter()` method to create an array of nodes that have even values.
3. If the `evenNodes` array is empty, it means that there are no even values in the input array. In this case, we return an empty array.
4. We use the `Math.min()` function to find the smallest even value in the `evenNodes` array.
5. We use the `indexOf()` method to find the index of the smallest even value in the original input array.
6. We return an array containing the smallest even value and its index.

You can test this function with the examples provided in the problem statement to see that it produces the correct output.