To solve the problem, we need to follow these steps:

1. Filter the array to include only the numbers between 1 and 9.
2. Sort the filtered array in ascending order.
3. Reverse the sorted array.
4. Replace each number with its corresponding name from "One" to "Nine".
5. If the array is empty, return an empty array.

Here's how you can implement the `byLength` function:

```javascript
const byLength = (arr) => {
  // Filter the array to include only numbers between 1 and 9
  const filteredArr = arr.filter(num => num > 0 && num < 10);

  // Sort the filtered array in ascending order
  const sortedArr = filteredArr.sort((a, b) => a - b);

  // Reverse the sorted array
  const reversedArr = sortedArr.reverse();

  // Replace each number with its corresponding name
  const numberToName = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
  };
  const result = reversedArr.map(num => numberToName[num]);

  return result;
};
```

Let's test the function with the provided examples:

```javascript
console.log(byLength([2, 1, 1, 4, 5, 8, 2, 3])); // ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
console.log(byLength([])); // []
console.log(byLength([1, -1, 55])); // ["One"]
```

This should give you the expected output for each test case.