```
  if (!l.length) {
    throw new Error('List is empty');
  }

  const sorted = l.slice().sort((a, b) => a - b);
  const middle = Math.floor(sorted.length / 2);

  if (sorted.length % 2 === 0) {
    return (sorted[middle - 1] + sorted[middle]) / 2;
  }

  return sorted[middle];
}
```


Explanation:
1. First, we check if the list is empty. If it is, we throw an error.
2. Then, we sort the list in ascending order.
3. We calculate the middle index of the sorted list. If the list length is even, the median will be the average of the two middle elements. If the list length is odd, the median will be the middle element.
4. We return the median value. If the list length is even, we return the average of the two middle elements. If the list length is odd, we return the middle element.

Example:
```
median([3, 1, 2, 4, 5])  # 3
median([-10, 4, 6, 1000, 10, 20])  # 8.0
```


Testing:
```
assert(median([3, 1, 2, 4, 5]) == 3)
assert(median([-10, 4, 6, 1000, 10, 20]) == 8.0)
```


Note:
The median is a robust measure of central tendency, as it is not affected by extreme values in the list. The median is also a good measure of central tendency when the list contains outliers or skewed data. However, the median is not the only measure of central tendency, and it may not always be the best choice depending on the specific problem or data set.