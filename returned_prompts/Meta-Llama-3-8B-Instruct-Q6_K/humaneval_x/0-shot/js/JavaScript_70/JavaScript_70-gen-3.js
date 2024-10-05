```
const strangeSortList = (lst) => {
  if (lst.length === 0) return [];

  const sortedList = lst.slice().sort((a, b) => a - b);
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


Explanation:
This function takes a list of integers as an argument. It first checks if the list is empty, in which case it returns an empty list.

Next, it creates a sorted copy of the list using the `slice()` method and the `sort()` method. This sorted list will be used to create the strange sorted list.

The function then initializes an empty list `result` that will be used to store the strange sorted list.

The function then enters a loop that continues until the `sortedList` is empty. In each iteration of the loop, it adds the smallest element from the `sortedList` to the `result` list using `shift()`. Then, if the `sortedList` is not empty, it adds the largest element from the `sortedList` to the `result` list using `pop()`.

Finally, the function returns the `result` list, which is the strange sorted list.