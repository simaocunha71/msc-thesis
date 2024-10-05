The problem asks you to write a function that returns the 2nd smallest element in a list of integers. If the list contains less than two elements, the function should return null.

Here is a JavaScript solution for this problem:

```javascript
const nextSmallest = (lst) => {
  if (lst.length < 2) {
    return null;
  }
  lst.sort((a, b) => a - b);
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] > lst[0]) {
      return lst[i];
    }
  }
  return null;
};
```

This function first checks if the list contains less than two elements. If it does, it returns null. Otherwise, it sorts the list in ascending order. Then, it iterates over the list starting from the second element (index 1). If it finds an element that is greater than the smallest element, it returns that element, which is the 2nd smallest element in the list. If it doesn't find such an element, it returns null, which means the list contains less than two distinct elements.