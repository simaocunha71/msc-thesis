You can solve this problem using a JavaScript function that iterates over the input list `numbers` and inserts the `delimeter` between every two consecutive elements. Here's the solution:
```
const intersperse = (numbers, delimeter) => {
  return numbers.reduce((acc, current, index) => {
    if (index < numbers.length - 1) {
      return acc.concat([current, delimeter]);
    } else {
      return acc.concat([current]);
    }
  }, []);
};
```
Here's an explanation of how the function works:

1. The function takes two arguments: `numbers` (the input list) and `delimeter` (the number to be inserted between elements).
2. The function uses the `reduce()` method to iterate over the input list `numbers`.
3. Inside the callback function, we check if the current index is less than the length of the list minus one (`numbers.length - 1`). This is because we want to insert the `delimeter` between every two consecutive elements, so we stop inserting `delimeter` after the second-to-last element.
4. If the condition is true, we concatenate the current element with the `delimeter` to the accumulator array (`acc`). If the condition is false, we simply concatenate the current element to the accumulator array.
5. The `reduce()` method returns the final accumulator array, which is the modified input list with the `delimeter` inserted between every two consecutive elements.

You can test the function with the provided examples:
```
console.log(intersperse([], 4)); // []
console.log(intersperse([1, 2, 3], 4)); // [1, 4, 2, 4, 3]
```



