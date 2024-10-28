```
const pluck = (arr) => {
  if (arr.length === 0) return [];

  const evenNodes = arr.filter(node => node % 2 === 0);
  if (evenNodes.length === 0) return [];

  const smallestValue = Math.min(...evenNodes);
  const smallestIndex = arr.indexOf(smallestValue);

  return [smallestValue, smallestIndex];
};
```
Explanation:
The code defines a function `pluck` that takes an array of nodes as input. It first checks if the array is empty, and if so, returns an empty array.

Next, it filters the array to get an array of even nodes using the `filter` method and the condition `node % 2 === 0`. If no even nodes are found, it returns an empty array.

If even nodes are found, it uses the `Math.min` function to find the smallest value among the even nodes. It then uses the `indexOf` method to find the index of the smallest value in the original array.

Finally, it returns an array containing the smallest value and its index.

The time complexity of this solution is O(n), where n is the length of the input array, because it needs to iterate over the array twice: once to filter the even nodes and once to find the smallest value and its index. The space complexity is O(n) as well, because in the worst case, the filtered array can have the same length as the original array.