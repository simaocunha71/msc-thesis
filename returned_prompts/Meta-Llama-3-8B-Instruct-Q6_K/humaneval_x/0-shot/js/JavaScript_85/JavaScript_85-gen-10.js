Here is a simple function that solves the problem:
```javascript
const add = (lst) => {
  let sum = 0;
  for (let i = 1; i < lst.length; i += 2) {
    if (lst[i] % 2 === 0) {
      sum += lst[i];
    }
  }
  return sum;
};
```
Here's an explanation of the code:

* We initialize a variable `sum` to 0, which will store the sum of the even elements at odd indices.
* We use a `for` loop to iterate over the list, starting from the second element (index 1) and incrementing by 2 each time. This ensures that we only consider elements at odd indices.
* Inside the loop, we check if the current element is even by using the modulo operator (`%`). If it's even, we add it to the `sum` variable.
* Finally, we return the `sum` variable.

Let's test the function with the example you provided:
```javascript
console.log(add([4, 2, 6, 7])); // Output: 2
```
It works! 😊

Note that this function assumes that the input list is non-empty. If you want to handle the case where the input list is empty, you can add a simple check at the beginning of the function:
```javascript
const add = (lst) => {
  if (lst.length === 0) {
    return 0; // or any other default value you prefer
  }
  // rest of the function remains the same
};
```