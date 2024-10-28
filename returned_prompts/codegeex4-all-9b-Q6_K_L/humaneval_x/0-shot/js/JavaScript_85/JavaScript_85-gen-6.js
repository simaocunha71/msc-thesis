Here's one way to do it:

```javascript
const add = (lst) => {
  let sum = 0;
  for (let i = 1; i < lst.length; i += 2) {
    if (lst[i] % 2 === 0) {
      sum += lst[i];
    }
  }
  return sum;
};
```

This function iterates through the list starting at index 1 (the first odd index) and increments by 2 each time to get the next odd index. If the element at that index is even, it's added to the sum. Finally, the sum is returned.