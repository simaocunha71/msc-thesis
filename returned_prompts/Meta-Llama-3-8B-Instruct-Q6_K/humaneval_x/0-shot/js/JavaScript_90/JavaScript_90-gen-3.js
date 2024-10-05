```
const nextSmallest = (lst) => {
  if (lst.length < 2) return null;
  lst.sort((a, b) => a - b);
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] !== lst[i - 1]) {
      return lst[i];
    }
  }
  return null;
};
```


Explanation:
The function `nextSmallest` takes a list of integers as an argument. It first checks if the list has less than 2 elements. If it does, it returns `null`, as there is no 2nd smallest element.

If the list has 2 or more elements, it sorts the list in ascending order. Then, it iterates over the sorted list starting from the second element (at index 1). If it finds an element that is different from the previous one, it returns that element, which is the 2nd smallest in the list.

If the function reaches the end of the list without finding a unique element, it returns `null`, indicating that there is no 2nd smallest element.

This solution has a time complexity of O(n log n) due to the sorting operation, where n is the length of the input list. The subsequent iteration over the sorted list has a time complexity of O(n), but since it is dominated by the sorting operation, it can be ignored. The space complexity is O(1) as it only uses a constant amount of space to store the index and the current element.