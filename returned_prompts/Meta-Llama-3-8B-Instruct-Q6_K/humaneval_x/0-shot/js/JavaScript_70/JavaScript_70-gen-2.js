```
const strangeSortList = (lst) => {
  if (lst.length === 0) return [];
  const sorted = lst.slice().sort((a, b) => a - b);
  const result = [];
  let minIndex = 0;
  let maxIndex = sorted.length - 1;

  while (sorted.length > 0) {
    result.push(sorted[minIndex]);
    sorted.splice(minIndex, 1);
    if (sorted.length > 0) {
      result.push(sorted[maxIndex]);
      sorted.splice(maxIndex, 1);
    }
    minIndex = sorted.indexOf(Math.min(...sorted));
    maxIndex = sorted.indexOf(Math.max(...sorted));
  }

  return result;
};
```


This code works by first sorting the input list in ascending order. Then it creates an empty result list and two indices, `minIndex` and `maxIndex`, to keep track of the minimum and maximum values in the sorted list.

It then enters a loop where it adds the minimum value to the result list, removes it from the sorted list, adds the maximum value (if the list is not empty) to the result list, removes it from the sorted list, and updates `minIndex` and `maxIndex` to the new minimum and maximum values.

This process is repeated until the sorted list is empty, at which point the result list contains the input list in the "strange" order. The `Math.min(...sorted)` and `Math.max(...sorted)` expressions are used to find the minimum and maximum values in the sorted list, and the `indexOf` method is used to find the indices of these values. The `splice` method is used to remove the values from the sorted list. The `push` method is used to add the values to the result list.