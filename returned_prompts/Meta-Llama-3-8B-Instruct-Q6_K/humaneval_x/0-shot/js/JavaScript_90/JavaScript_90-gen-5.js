```
const nextSmallest = (lst) => {
  if (lst.length === 0) return null;
  lst.sort((a, b) => a - b);
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] !== lst[0]) return lst[i];
  }
  return null;
};
```


Explanation:
The function takes a list of integers as input. First, it checks if the list is empty. If it is, the function returns null. Then, it sorts the list in ascending order. After that, it iterates through the list starting from the second element (index 1). If it finds an element that is not equal to the smallest element in the list (which is at index 0), it returns that element as the 2nd smallest. If it doesn't find any such element, it returns null. This is because the list either has less than two unique elements or all elements are the same, which means there is no 2nd smallest element.