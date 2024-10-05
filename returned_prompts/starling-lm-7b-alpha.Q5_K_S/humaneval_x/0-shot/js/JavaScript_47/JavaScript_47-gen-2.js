To solve this problem, you can follow these steps:

1. Sort the list in ascending order. You can use the `sort()` method to do this. The `sort()` method modifies the original list in place. If you don't want to modify the original list, you can create a copy of the list using the `slice()` method and then sort the copy.

2. Calculate the median. The median is the middle value in a sorted list. If the length of the list is odd, the median is the value at the index `Math.floor(l.length / 2)`. If the length of the list is even, the median is the average of the values at the indices `Math.floor(l.length / 2)` and `Math.floor((l.length - 1) / 2)`.

3. Return the calculated median.

Here's a detailed solution using these steps:

```javascript
const median = (l) => {
  // Sort the list in ascending order
  l.sort((a, b) => a - b);

  // Calculate the median
  const length = l.length;
  if (length % 2 === 0) {
    return (l[length / 2] + l[(length - 1) / 2]) / 2;
  } else {
    return l[Math.floor(length / 2)];
  }
};
```

You can test the `median` function with the provided test cases:

```javascript
console.log(median([3, 1, 2, 4, 5]));  // Output: 3
console.log(median([-10, 4, 6, 1000, 10, 20]));  // Output: 8.0
```

These test cases will verify if the `median` function is correctly calculating the median of the given lists.

The time complexity of this function is O(n log n), where n is the length of the list. This is because the `sort()` method has a time complexity of O(n log n).

The space complexity of this function is O(1), as it does not use any additional space