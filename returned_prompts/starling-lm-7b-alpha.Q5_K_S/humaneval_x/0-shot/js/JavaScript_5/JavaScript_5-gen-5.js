Here is one possible solution using JavaScript:

```javascript
const intersperse = (numbers, delimeter) => {
  const result = [];
  for (let i = 0; i < numbers.length; i++) {
    result.push(numbers[i]);
    if (i !== numbers.length - 1) {
      result.push(delimeter);
    }
  }
  return result;
};
```

This solution uses a for loop to iterate through the input list `numbers`. It pushes each number to a new array `result`. After each number, it checks if it is the last number in the list. If it's not the last number, it pushes the `delimeter` to the `result` array. Finally, it returns the `result` array.

For example, if we call `intersperse([1, 2, 3], 4)`, it will return `[1, 4, 2, 4, 3]`.

Here are some additional test cases to verify the solution:

```javascript
console.log(intersperse([], 4));  // []
console.log(intersperse([1, 2, 3], 4));  // [1, 4, 2, 4, 3]
console.log(intersperse([1, 2, 3, 4], 4));  // [1, 4, 2, 4, 3, 4]
console.log(intersperse([1, 2, 3, 4, 5], 4));  // [1, 4, 2, 4, 3, 4, 5]
```

The solution correctly intersperse the `delimeter` between every two consecutive elements of the input list.

In this solution, we use a for loop to iterate through the input list `numbers`. For each element in the list, we push it to a new array `result`. After pushing the element, we check if it is the last element in the list. If it's not the last element, we push the `delimeter` to the `result` array. Finally, we return the `result` array, which contains the