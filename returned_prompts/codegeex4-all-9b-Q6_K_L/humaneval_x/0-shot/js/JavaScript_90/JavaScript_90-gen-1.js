You can solve this problem by using a set to remove duplicates from the list and then find the second smallest number. Here is the JavaScript code for it:

```javascript
const nextSmallest = (lst) => {
  let arr = [...new Set(lst)].sort((a, b) => a - b);
  return arr.length > 1 ? arr[1] : null;
};
```

This code first removes duplicates from the list by converting it to a set and then back to an array. Then it sorts the array in ascending order. Finally, it checks if the length of the array is greater than 1. If it is, it returns the second element of the array. If it is not, it returns null.