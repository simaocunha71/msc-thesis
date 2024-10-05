To intersperse a delimiter between every two consecutive elements of a given list, you can use the following JavaScript function:

```javascript
function intersperse(numbers, delimeter) {
  return numbers.map((num, index) => index % 2 === 0 ? [num].concat(delimeter) : [num]);
}
```

The `intersperse` function takes in two parameters: `numbers` (the input list) and `delimeter` (the number to be inserted between each element). 

Inside the function, we use the `map` method to iterate over each element in the `numbers` array. For each element, we check if the index is even (`index % 2 === 0`). If the index is even, we concatenate the current element with the `delimeter` using the `concat` method and return it as an array. If the index is odd, we simply return the current element as an array. 

Finally, the `map` method returns a new array with the modified elements, and this array is returned as the result.

For example, if we call `intersperse([1, 2, 3], 4)`, it will return `[1, 4, 2, 4, 3]` as the delimiter is interspersed between each element of the input list.

Hope this helps! Let me know if you have any more questions.
```
```

Here is another solution using `reduce`:

```javascript
function intersperse(numbers, delimeter) {
  return numbers.reduce((acc, cur, idx) => {
    if (idx % 2 === 0) {
      acc.push(cur);
    } else {
      acc.push(cur, delimeter);
    }
    return acc;
  }, []);
}
```

In this version of the function, we use the `reduce` method to iterate over each element in the `numbers` array. We pass an empty array `[]` as the initial value for the accumulator `acc`. 

Inside the `reduce` method, we check if the index of the current element is even (`idx % 2 === 