```javascript
const doubleTheDifference = (lst) => {
  return lst.filter((num) => num % 2 !== 0 && num >= 0 && typeof num === 'number')
    .map((num) => num ** 2)
    .reduce((acc, curr) => acc + curr, 0);
};
```



Explanation:

The problem asks to find the sum of squares of odd numbers in a list, ignoring negative numbers and non-integers. We can solve this by using the `filter`, `map`, and `reduce` methods.

1. `filter` method is used to filter out the numbers that are not odd, negative or non-integer. We use the condition `num % 2 !== 0 && num >= 0 && typeof num === 'number'` to filter out the numbers.
2. `map` method is used to square each of the filtered numbers.
3. `reduce` method is used to sum up the squared numbers. We initialize the accumulator `acc` to 0 and add each squared number to it.

The `doubleTheDifference` function takes a list as an argument and returns the sum of squares of the odd numbers in the list that are not negative or non-integer. If the input list is empty, it returns 0.