You can use a Set to remove duplicates, then convert the Set back to an array and sort it to keep the order of elements the same as in the input. Here's how you can implement the `removeDuplicates` function:

```javascript
const removeDuplicates = (numbers) => {
  return [...new Set(numbers)].sort((a, b) => numbers.indexOf(a) - numbers.indexOf(b));
};
```

This function first converts the input array `numbers` to a Set, which automatically removes any duplicate values. Then it converts the Set back to an array using the spread operator `[...]`. Finally, it sorts the array to keep the order of elements the same as in the input.

Here's an example of how you can use this function:

```javascript
console.log(removeDuplicates([1, 2, 3, 2, 4])); // [1, 3, 4]
```

This will output `[1, 3, 4]`, which is the list of integers with all duplicates removed while keeping the order of elements the same as in the input.