The solution to this problem can be found in the following JavaScript code:

```javascript
const nextSmallest = (lst) => {
  if (lst.length < 2) return null;
  lst.sort((a, b) => a - b);
  let smallest = lst[0];
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] !== smallest) {
      return lst[i];
    }
  }
  return null;
};
```

In this solution, we first check if the list has less than 2 elements. If it does, we return null. Then, we sort the list in ascending order. We keep track of the smallest element and iterate through the list. If we find an element that is not equal to the smallest, we return it. If we reach the end of the list without finding a new smallest element, we return null. This way, we find the 2nd smallest element in the list. If the list has less than 2 unique elements, we return null.