```
const nextSmallest = (lst) => {
  if (lst.length < 2) {
    return null;
  }
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
The function first checks if the list has less than 2 elements. If so, it returns null. Then it sorts the list in ascending order. It then iterates over the list, starting from the second element, and checks if the current element is different from the previous one. If it finds an element that is different from the previous one, it returns that element as the 2nd smallest. If it doesn't find any such element, it means the list has all duplicates or only one unique element, so it returns null.