```
const strangeSortList = (lst) => {
  if (lst.length === 0) return [];

  lst.sort((a, b) => {
    if (a < b) return -1;
    if (a > b) return 1;
    return 0;
  });

  let result = [];
  let minIndex = 0;
  let maxIndex = lst.length - 1;

  while (minIndex <= maxIndex) {
    result.push(lst[minIndex]);
    minIndex++;

    if (minIndex <= maxIndex) {
      result.push(lst[maxIndex]);
      maxIndex--;
    }
  }

  return result;
};
```


Explanation:

1. First, we sort the input list in ascending order. This ensures that the smallest value comes first, and the largest value comes last.
2. Then, we create an empty result list.
3. We initialize two pointers: `minIndex` and `maxIndex`. `minIndex` points to the smallest value in the sorted list, and `maxIndex` points to the largest value.
4. We iterate through the list, adding the smallest value to the result list and incrementing `minIndex`. Then, if `minIndex` is still within the bounds of the list, we add the largest value to the result list and decrement `maxIndex`.
5. We repeat step 4 until `minIndex` exceeds `maxIndex`, at which point the entire list has been processed.
6. Finally, we return the result list.

This approach ensures that the smallest value comes first, followed by the largest value, then the second smallest value, and so on, resulting in the "strange" sorting order described in the problem.