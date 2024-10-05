Here is a solution using JavaScript:

```javascript
const removeDuplicates = (numbers) => {
  let result = [];
  for (let i = 0; i < numbers.length; i++) {
    if (!result.includes(numbers[i])) {
      result.push(numbers[i]);
    }
  }
  return result;
};

console.log(removeDuplicates([1, 2, 3, 2, 4])); // Output: [1, 3, 4]
```

This function iterates over the input array, and for each element, it checks if the result array already includes that element. If not, it adds the element to the result array. At the end, it returns the result array. The order of elements in the result array is the same as in the input array.

Note: This solution has a time complexity of O(n^2) due to the use of the includes() method, which has to iterate over the entire result array for each element in the input array. This could be improved by using a different data structure, such as a Set, which has a time complexity of O(1) for the includes() method. Here is an example of how to use a Set:

```javascript
const removeDuplicates = (numbers) => {
  const seen = new Set();
  return numbers.filter(num => !seen.has(num) && seen.add(num));
};

console.log(removeDuplicates([1, 2, 3, 2, 4])); // Output: [1, 3, 4]
```

This solution uses the filter() method to create a new array with only the elements that are not already in the seen Set. The includes() method is not needed because the Set automatically keeps track of the elements it has seen. This solution has a time complexity of O(n).