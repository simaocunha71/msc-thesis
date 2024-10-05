Here's how you might do it:

```javascript
const oddCount = (lst) => {
  return lst.map(str => {
    const count = str.split('').filter(digit => digit % 2 !== 0).length;
    return `the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`;
  });
}
```

The `map` function creates a new array by applying a function to each element of the input array. In this case, the function is a function that takes a string and returns a modified version of the string.

The `split('')` function splits a string into an array of its characters. The `filter` function then creates a new array that only includes the elements for which the function returns true. In this case, the function is a function that returns true for any digit that is odd (i.e., not divisible by 2).

The `length` property of an array gives the number of elements in the array. We then use this number to create a new string that includes the number of odd elements.

Finally, we return the new array.