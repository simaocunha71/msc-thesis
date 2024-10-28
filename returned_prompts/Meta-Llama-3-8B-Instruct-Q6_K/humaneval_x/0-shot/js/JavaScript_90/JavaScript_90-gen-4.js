```
const nextSmallest = (lst) => {
  if (!lst.length) return null;
  lst.sort((a, b) => a - b);
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] !== lst[i - 1]) {
      return lst[i];
    }
  }
  return null;
};
```


Explanation:
The function `nextSmallest` takes a list of integers as an argument. It first checks if the list is empty, in which case it returns null. Then it sorts the list in ascending order. 

It then iterates through the sorted list, starting from the second element (index 1). If it finds a number that is different from the previous one, it returns that number, which is the 2nd smallest element. If it doesn't find such an element (i.e., the list has only one unique element), it returns null.

Note: The function returns null when there is no 2nd smallest element, which is the case when the list has only one unique element or is empty. It also returns null when the list has multiple identical elements. For example, the list [1, 1] has no 2nd smallest element. 