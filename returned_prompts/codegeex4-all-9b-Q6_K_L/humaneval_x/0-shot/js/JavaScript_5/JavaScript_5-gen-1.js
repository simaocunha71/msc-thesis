You can solve this problem by using the reduce function in JavaScript. The reduce function applies a function to an accumulator and each element in the array (from left to right) to reduce it to a single output value. Here is how you can use it to solve this problem:

```javascript
const intersperse = (numbers, delimeter) => {
  return numbers.reduce((acc, val, idx) => {
    if (idx > 0) acc.push(delimeter);
    acc.push(val);
    return acc;
  }, []);
};
```

In this function, we start with an empty array as the initial accumulator value. Then, for each element in the input array, we check if it's not the first element (because we don't need to insert the delimeter before the first element). If it's not the first element, we push the delimeter to the accumulator. Then, we push the current element to the accumulator. Finally, we return the accumulator, which is the interspersed array.