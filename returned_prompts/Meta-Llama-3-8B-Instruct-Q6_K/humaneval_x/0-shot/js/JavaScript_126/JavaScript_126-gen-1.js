Here is the solution in JavaScript:
```
const isSorted = (lst) => {
  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] >= lst[i + 1]) {
      for (let j = 0; j < i; j++) {
        if (lst[j] === lst[i]) {
          return false;
        }
      }
    } else {
      return false;
    }
  }
  return true;
};
```
Explanation:

1. We iterate through the list from the first element to the second last element.
2. For each element, we check if it is greater than or equal to the next element. If it is not, we immediately return `false` because the list is not sorted.
3. If the current element is less than or equal to the next element, we check if there are any duplicates of the current element before it. If there are, we return `false` because the list is not sorted.
4. If the list passes all the above checks, we return `true` because the list is sorted.

Note: This solution assumes that the input list only contains positive integers. If the list can contain negative numbers or non-integer values, additional checks would be needed.