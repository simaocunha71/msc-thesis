Here is the solution to the problem:

```javascript
const isSorted = (lst) => {
  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] >= lst[i + 1]) {
      if (lst.filter(x => x === lst[i]).length > 1) {
        return false;
      }
    } else {
      return false;
    }
  }
  return true;
};
```


Explanation:

The function `isSorted` takes a list of numbers as an argument. It iterates over the list, checking each number with the next one. If any number is greater than or equal to the next one, it means the list is not sorted in ascending order, so the function returns `false`. If a duplicate number is found, the function also returns `false`. If the function reaches the end of the list without finding any non-ascending pairs or duplicates, it returns `true`, indicating that the list is sorted in ascending order.