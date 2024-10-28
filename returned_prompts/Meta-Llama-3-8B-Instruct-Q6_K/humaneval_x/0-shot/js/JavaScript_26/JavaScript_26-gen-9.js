Here is a solution using the Set data structure in JavaScript:
```
const removeDuplicates = (numbers) => {
  const seen = new Set();
  return numbers.filter(num => !seen.has(num) && seen.add(num));
};
```
Here's an explanation of how the code works:

1. We create a new Set `seen` to keep track of the unique elements we've seen so far.
2. We use the `filter()` method to iterate over the input array `numbers`.
3. For each element `num` in the array, we check if it's already in the `seen` set using the `has()` method. If it is, we skip it.
4. If it's not in the set, we add it to the set using the `add()` method and return the element.
5. The resulting array will only contain the unique elements in the original order.

Here's an example usage:
```
console.log(removeDuplicates([1, 2, 3, 2, 4])); // [1, 3, 4]
```
Note that this solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input array. This is because we need to iterate over the entire array and store the unique elements in the `seen` set. However, this is the most efficient solution for this problem, as we need to iterate over the array at least once to find the duplicates.