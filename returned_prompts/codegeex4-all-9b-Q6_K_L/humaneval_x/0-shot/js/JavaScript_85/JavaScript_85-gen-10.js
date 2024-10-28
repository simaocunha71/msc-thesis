You can use the reduce function to sum up the even elements at odd indices. Here's how you can do it:

```javascript
const add = (lst) => {
  return lst.reduce((acc, val, idx) => {
    if (idx % 2 !== 0 && val % 2 === 0) {
      return acc + val;
    } else {
      return acc;
    }
  }, 0);
};
```

This code goes through the list using the reduce function and checks if the index is odd and the value is even. If both conditions are true, it adds the value to the accumulator.