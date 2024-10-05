You can create a new array with the numbers between 1 and 9, sort it, reverse it and then map each number to its corresponding name. Here is how you can do it:

```javascript
const byLength = (arr) => {
  const numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
  return arr
    .filter((num) => num >= 1 && num <= 9)
    .sort((a, b) => a - b)
    .reverse()
    .map((num) => numbers[num - 1]);
};
```

In the function above, first we filter out the numbers that are between 1 and 9 using the `filter` function. Then we sort the filtered array in ascending order with the `sort` function. After that, we reverse the sorted array with the `reverse` function. Finally, we map each number to its corresponding name using the `map` function.