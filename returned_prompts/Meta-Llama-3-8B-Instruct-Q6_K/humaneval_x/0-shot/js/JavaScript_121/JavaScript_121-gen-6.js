The function takes a list of integers as input. It iterates over the list using a for loop, and checks if the current index is even. If the current index is even and the current element is odd, it adds the element to the sum. The function returns the sum of all the odd elements that are in even positions.

Here is the JavaScript code for the solution:

```javascript
const solution = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 === 0 && lst[i] % 2 !== 0) {
      sum += lst[i];
    }
  }
  return sum;
};
```

Let's test this function with the examples provided:

```javascript
console.log(solution([5, 8, 7, 1])); // Output: 12
console.log(solution([3, 3, 3, 3, 3])); // Output: 9
console.log(solution([30, 13, 24, 321])); // Output: 0
```

The function works correctly and returns the expected results. It successfully sums up all the odd elements that are in even positions in the list. 