Here is the solution:
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
Here's an explanation of the code:

* We initialize a variable `sum` to 0, which will store the sum of all the odd elements in even positions.
* We iterate through the list using a `for` loop, with `i` as the index.
* We check if the current index `i` is even using the condition `i % 2 === 0`. This will be true if the index is 0, 2, 4, etc.
* We also check if the element at the current index is odd using the condition `lst[i] % 2 !== 0`. This will be true if the element is 1, 3, 5, etc.
* If both conditions are true, we add the element to the `sum`.
* Finally, we return the `sum`.

Let's test this function with the examples provided:

```javascript
console.log(solution([5, 8, 7, 1])); // Output: 12
console.log(solution([3, 3, 3, 3, 3])); // Output: 9
console.log(solution([30, 13, 24, 321])); // Output: 0
```
The function works as expected! 😊