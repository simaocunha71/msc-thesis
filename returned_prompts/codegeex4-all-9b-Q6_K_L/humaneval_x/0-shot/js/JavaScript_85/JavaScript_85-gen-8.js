You can solve this problem by using the reduce method in combination with the filter and modulo operators. Here's how:

```javascript
const add = (lst) => {
  return lst.reduce((acc, val, idx) => {
    return idx % 2 === 1 && val % 2 === 0 ? acc + val : acc;
  }, 0);
}
```

In this solution, we start by initializing the accumulator (acc) to 0. Then, for each element in the array, we check if its index is odd (idx % 2 === 1) and if the element itself is even (val % 2 === 0). If both conditions are true, we add the value to the accumulator. Finally, we return the accumulator.