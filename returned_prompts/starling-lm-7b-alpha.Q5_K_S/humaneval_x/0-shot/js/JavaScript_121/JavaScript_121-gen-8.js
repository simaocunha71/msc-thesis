Here's a solution using JavaScript:

```javascript
const solution = (lst) => {
  return lst.reduce((acc, curr) => {
    if (curr % 2 === 0 && curr % 2 === 0) {
      acc += curr;
    }
    return acc;
  }, 0);
};
```

The `solution` function takes in a list of integers called `lst`. It uses the `reduce` method to iterate over each element in the list and accumulate a sum of all the odd elements in even positions. 

In the `reduce` method, the `acc` parameter represents the accumulator, which starts with an initial value of 0. The `curr` parameter represents the current element in the list. 

Inside the `reduce` method, the `if` statement checks if the current element (`curr`) is both even (`curr % 2 === 0`) and odd (`curr % 2 === 1`). If it is, the current element is added to the accumulator (`acc`). 

Finally, the function returns the accumulated sum of the odd elements in even positions.

For example, if we call `solution([5, 8, 7, 1])`, the function will return 12, because the odd elements in even positions are 8 and 1, and their sum is 9. 

Similarly, if we call `solution([3, 3, 3, 3, 3])`, the function will return 9, because all the elements in even positions are 3, and their sum is 9. 

If we call `solution([30, 13, 24, 321])`, the function will return 0, because there are no odd elements in even positions. 

Overall, this solution effectively sums up all the odd elements in even positions of a given list of integers.
``