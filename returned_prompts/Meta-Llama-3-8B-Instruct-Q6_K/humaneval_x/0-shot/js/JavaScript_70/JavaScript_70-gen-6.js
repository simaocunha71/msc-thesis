Here is the solution for the problem. This function takes a list of integers as an argument and returns the list in a strange order. The strange order is determined by alternating between the smallest and largest elements in the list.

```
const strangeSortList = (lst) => {
  if (lst.length === 0) return [];

  const sortedList = lst.sort((a, b) => a - b);
  const result = [];

  while (sortedList.length > 0) {
    result.push(sortedList.shift());
    if (sortedList.length > 0) {
      result.push(sortedList.pop());
    }
  }

  return result;
};
```

This function works by first sorting the list in ascending order. Then it creates an empty result list and iterates over the sorted list, pushing the smallest element onto the result list, then the largest element, and so on. The result list is returned at the end.

Here are some examples of how this function works:

```
console.log(strangeSortList([1, 2, 3, 4])); // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); // [5, 5, 5, 5]
console.log(strangeSortList([])); // []
```

I hope this helps! Let me know if you have any questions.