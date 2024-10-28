Here is my solution:

1. Initialize a variable sum to 0.
2. Iterate through the list and for each element in the list do the following:
  a. Check if the index of the element is even. If yes, then check if the element is odd. If it's both, then add the element to the sum.
3. Return the sum.


Code:

```javascript
const solution = (lst) => {
  let sum = 0;

  for (let i = 0; i < lst.length; i++) {
   