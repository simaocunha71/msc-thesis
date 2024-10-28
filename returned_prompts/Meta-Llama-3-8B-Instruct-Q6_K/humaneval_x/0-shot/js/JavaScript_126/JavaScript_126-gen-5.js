Here is the solution using JavaScript:

```javascript
const isSorted = (lst) => {
  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] >= lst[i + 1]) {
      if (lst.slice(i).filter((x, index) => x === lst[i]).length > 1) {
        return false;
      }
    } else {
      return false;
    }
  }
  return true;
};
```

This function iterates through the list and checks if each element is less than or equal to the next one. If it finds an element that is not less than or equal to the next one, it returns `false`. If it doesn't find any such elements, it checks if there are any duplicate elements in the list by filtering the list starting from the current index and returning `false` if it finds more than one duplicate. If it doesn't find any duplicate elements, it returns `true`. This solution assumes that the list only contains integers and no negative numbers. If the list can contain negative numbers, additional checks are needed. If the list can contain non-integer values, additional checks are also needed.