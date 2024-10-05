You can solve this problem by first creating a new array that contains only the even elements from the input array. Then, you can filter the new array to only include elements at odd indices. Finally, you can use the reduce method to sum up the elements in the filtered array.

Here's the solution:

```javascript
const add = (lst) => {
  const evenElements = lst.filter(num => num % 2 === 0);
  const oddIndices = evenElements.filter((num, index) => index % 2 !== 0);
  return oddIndices.reduce((sum, num) => sum + num, 0);
}
```

In this code, the `filter` method is used to create two new arrays: `evenElements` and `oddIndices`. The `reduce` method is then used to sum up the elements in the `oddIndices` array and return the result.