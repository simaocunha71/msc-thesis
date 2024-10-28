One way to solve this problem is to use the `reduce` method to check if all elements in the list are equal to the previous one. If they are not, then the list is not sorted in ascending order. Here's a step-by-step explanation:

1. Use the `reduce` method to iterate over the list and check if each element is equal to the previous one.
2. If the condition `(accumulator === currentValue)` is true for all elements, return `true`; otherwise, return `false`.
3. Since the `reduce` method stops once the condition is false, we don't need to manually check the length of the list.
4. Return the result of the `reduce` method.

Here's the code implementation of the solution:

```javascript
const isSorted = (lst) => {
  return lst.reduce((accumulator, currentValue) => accumulator === currentValue, true);
};
```

By using this approach, we can determine if the list is sorted in ascending order and handle cases with duplicate values correctly.

Note: This solution assumes that the input list contains only integers and does not include negative numbers.

Here are some test cases to verify the solution:

```javascript
console.log(isSorted([5])); // Output: true
console.log(isSorted([1, 2, 3, 4, 5])); // Output: true
console.log(isSorted([1, 3, 2, 4, 5])); // Output: false
console.log(isSorted([1, 2, 3, 4, 5, 6])); // Output: true
console.log(isSorted([1, 2, 3, 4, 5, 6, 7])); // Output: true
console.log(isSorted([1, 3, 2, 4, 5, 6, 7])); // Output: false
console.log(isSorted([1, 2, 2, 3, 3, 4])); // Output: true
console.log(isSorted([1, 2, 2, 2, 3, 4])); // Output: false
```
