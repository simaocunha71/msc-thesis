To solve this problem, we can use a Set to keep track of unique elements as we iterate through the input array. Here's a step-by-step breakdown of the solution:

1. Declare an empty Set called "seen" to keep track of unique elements.
2. Iterate through the input array using a for loop.
3. For each element, check if it's already in the "seen" Set. If it's not, add it to the Set.
4. If the element is not in the Set, push it into a new array called "result". This array will hold the unique elements in the same order as they appear in the input array.
5. After iterating through all elements, return the "result" array.

Here's the code implementation:

```javascript
const removeDuplicates = (numbers) => {
  const seen = new Set();
  const result = [];

  for (const num of numbers) {
    if (!seen.has(num)) {
      seen.add(num);
      result.push(num);
    }
  }

  return result;
};
```

This solution has a time complexity of O(n), where n is the number of elements in the input array. The Set data structure allows for efficient lookup and addition operations, making this solution efficient.

The space complexity of this solution is also O(n), as we are storing all the unique elements in the "seen" Set and the "result" array.

Overall, this solution effectively removes all duplicate elements from the input array while maintaining the original order of the elements.

To use this solution, you can call the `removeDuplicates` function and pass in the input array as an argument. The function will return a new array with all duplicate elements removed, while preserving the order of the elements.

For example, if you call `removeDuplicates([1, 2, 3, 2, 4])`, the function will return `[1, 3, 4]`, as it removes the duplicate element 2 from the input array while maintaining the order of the remaining elements.

Hope this helps! Let me know if you have any more questions.

Best,
[Your Name]

P.S. Here