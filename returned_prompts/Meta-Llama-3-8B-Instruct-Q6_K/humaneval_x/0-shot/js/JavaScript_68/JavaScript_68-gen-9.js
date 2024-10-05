Here is a JavaScript solution that fulfills the requirements:

```javascript
const pluck = (arr) => {
  const evenNodes = arr.filter(node => node % 2 === 0);
  if (evenNodes.length === 0) return [];
  const smallestEvenValue = Math.min(...evenNodes);
  return [smallestEvenValue, arr.indexOf(smallestEvenValue)];
};
```

Explanation:

1. We first filter the array to get all the even nodes. This is done using the `filter()` method and a callback function that checks if the node value is even.
2. If there are no even nodes, we return an empty array.
3. We then find the smallest even value using the `Math.min()` function with the spread operator (`...`) to get the minimum value from the array of even nodes.
4. Finally, we return an array with the smallest even value and its index in the original array. We use the `indexOf()` method to get the index of the smallest even value.

The time complexity of this solution is O(n), where n is the number of nodes in the array. This is because we are iterating over the array twice: once to filter the even nodes and once to find the smallest even value and its index. The space complexity is O(n) as well, as we are storing the even nodes in a separate array.