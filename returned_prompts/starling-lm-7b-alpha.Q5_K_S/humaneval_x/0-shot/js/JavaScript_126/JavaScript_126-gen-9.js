To solve this problem, we need to compare each element in the list with its adjacent element. If the adjacent element is less than the current element, then the list is not sorted. If the adjacent element is greater than the current element, then the list is sorted. We also need to check if there are any duplicate values in the list. If there are duplicate values, then the list is not sorted.

Here's a step-by-step breakdown of the solution:

1. Initialize a variable `prev` to the first element of the list.
2. Iterate through the list starting from the second element.
3. Compare the current element with its adjacent element.
4. If the adjacent element is less than the current element, return `false`.
5. If the adjacent element is greater than the current element, return `true`.
6. Check if there are any duplicate values in the list. If there are duplicate values, return `false`.
7. If all elements are compared and no duplicates are found, return `true`.

Here's the code implementation of the solution:

```javascript
const isSorted = (lst) => {
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < lst[i - 1]) {
      return false;
    }
  }
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] === lst[i - 1]) {
      return false;
    }
  }
  return true;
};
```

This function will return `true` if the list is sorted in ascending order and does not have any duplicate values. Otherwise, it will return `false`.

You can use this function to check if a given list is sorted in ascending order and does not have duplicate values.









/* Given a list of numbers, return whether or not they are sorted
  in ascending order. If list has more than 1 duplicate of the same
  number, return false. Assume no negative numbers and only integers.
  Examples
  isSorted([5]) ➞ true
  isSorted([1, 2, 3, 4, 5