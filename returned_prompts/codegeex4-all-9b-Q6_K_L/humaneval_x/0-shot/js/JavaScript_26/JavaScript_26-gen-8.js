You can use the `filter` method along with `indexOf` to achieve this. Here's how you can modify the `removeDuplicates` function:

```javascript
const removeDuplicates = (numbers) => {
  return numbers.filter((num, index) => numbers.indexOf(num) === index);
};
```

The `filter` method creates a new array with all elements that pass the test implemented by the provided function. In this case, we are checking if the index of the current element is equal to its first occurrence in the array. If it's true, the element is included in the new array. If it's false, the element is not included.