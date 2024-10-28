```
const nextSmallest = (lst) => {
  if (lst.length < 2) return null;
  lst.sort((a, b) => a - b);
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] !== lst[0]) {
      return lst[i];
    }
  }
  return null;
};
```


Explanation:
1. We first check if the list has less than 2 elements. If it does, we return null.
2. We sort the list in ascending order.
3. We iterate through the list starting from the second element (index 1). We check each element to see if it is not equal to the smallest element (lst[0]).
4. If we find an element that is not equal to the smallest element, we return that element. This is because we've found the 2nd smallest element.
5. If we reach the end of the list without finding a 2nd smallest element, we return null.
6. If the list has only one unique element (e.g., [1, 1]), we return null because there is no 2nd smallest element.