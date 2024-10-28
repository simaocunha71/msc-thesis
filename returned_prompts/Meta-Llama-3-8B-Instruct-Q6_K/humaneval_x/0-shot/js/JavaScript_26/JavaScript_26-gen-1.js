```
const removeDuplicates = (numbers) => {
  const seen = {};
  return numbers.filter(num => {
    if (!seen[num]) {
      seen[num] = true;
      return true;
    }
    return false;
  });
};
```



Explanation:

*   We create an empty object `seen` to keep track of the numbers we've seen so far.
*   We use the `filter()` method to create a new array with the desired elements.
*   Inside the `filter()` callback, we check if the current number `num` is not present in the `seen` object. If it's not present, we set its value to `true` in the `seen` object and return `true` to include it in the new array.
*   If the number is already present in the `seen` object, we return `false` to exclude it from the new array.
*   The `filter()` method returns a new array with the unique elements, preserving the original order.

This solution has a time complexity of O(n), where n is the length of the input array, because we're iterating over the array once. The space complexity is O(n) as well, because we're storing the seen numbers in the `seen` object.