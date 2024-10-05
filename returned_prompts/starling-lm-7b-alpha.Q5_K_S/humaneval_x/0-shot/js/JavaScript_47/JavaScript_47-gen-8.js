To find the median of the list, first sort the list in ascending order. Then, if the length of the list is odd, return the element at the middle index. If the length of the list is even, return the average of the two middle elements.

In the first test case, the sorted list is [1, 2, 3, 4, 5]. Since the length is odd, the median is 3.

In the second test case, the sorted list is [-10, 4, 6, 10, 10, 20]. Since the length is even, the median is the average of the two middle elements, 10 and 10, which is 10.

Here's one way to implement this in JavaScript:

```javascript
const median = (l) => {
  const sorted = l.slice().sort((a, b) => a - b);
  const middleIndex = Math.floor(sorted.length / 2);
  const median = sorted.length % 2 === 0 ? (sorted[middleIndex - 1] + sorted[middleIndex]) / 2 : sorted[middleIndex];
  return median;
};
```

This implementation first creates a copy of the input list and sorts it in ascending order. Then, it calculates the index of the middle element (or elements, if the length is even) and returns the median value.

Note that this implementation uses the `slice()` method to create a copy of the input list to avoid modifying the original list. This is important because the `sort()` method sorts the list in place, which means it modifies the original list directly.

Also note that the comparison function `(a, b) => a - b` passed to the `sort()` method ensures that the list is sorted in ascending order.

Finally, the median is calculated as the average of the two middle elements if the length of the list is even (`sorted.length % 2 === 0`), and as the middle element if the length is odd (`sorted.length % 2 !== 0`).

This implementation should pass the tests you provided.
```

As an aside, if you're working with large lists, you might want to consider using