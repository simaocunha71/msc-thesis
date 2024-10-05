```javascript
const isSorted = (lst) => {
  for (let i = 1; i < lst.length; i++) {
    if (lst[i - 1] >= lst[i]) {
      if (lst.indexOf(lst[i]) !== lst.indexOf(lst[i - 1])) {
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

The function `isSorted` takes a list of integers as an argument. It iterates through the list, checking if each element is less than or equal to the previous one. If it finds a pair of elements where the previous one is greater than or equal to the current one, it immediately returns `false` because the list is not sorted. If it checks the entire list and doesn't find any such pairs, it returns `true` because the list is sorted.

The additional condition is to check for duplicate numbers. If a duplicate number is found, the function checks if it's the same as the previous number using the `indexOf` method. If they are the same, it returns `false` because the list has more than one duplicate of the same number. If they are not the same, it continues to check the rest of the list. If it doesn't find any duplicates, it returns `true` because the list is sorted and has no more than one duplicate of the same number.