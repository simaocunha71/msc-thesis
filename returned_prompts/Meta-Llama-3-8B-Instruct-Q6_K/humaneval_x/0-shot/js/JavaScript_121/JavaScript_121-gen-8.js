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
Explanation:
The function iterates over the list of integers and checks if the current index `i` is even (`i % 2 === 0`) and if the current element `lst[i]` is odd (`lst[i] % 2 !== 0`). If both conditions are true, it adds the element to the sum. The function returns the sum of all odd elements in even positions.

Note: The problem statement seems to be missing a detail, but based on the provided examples, it appears that the sum should be calculated for the elements at even positions (0-based indexing), and only the odd elements at these positions should be included in the sum. If this is not the intended interpretation, please clarify the problem statement.