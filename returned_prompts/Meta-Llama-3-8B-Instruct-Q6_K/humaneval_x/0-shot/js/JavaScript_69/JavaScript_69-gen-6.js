The function takes a list of integers as an argument and returns the greatest integer that is greater than zero and has a frequency greater than or equal to the value of the integer itself. If no such value exists, it returns -1.

Here is the implementation:
```
const search = (lst) => {
  let max = 0;
  for (let num of lst) {
    if (num > 0 && num <= lst.filter(x => x === num).length) {
      max = Math.max(max, num);
    }
  }
  return max > 0 ? max : -1;
};
```
Here's an explanation of the code:

1. We initialize a variable `max` to 0, which will store the greatest integer that meets the condition.
2. We iterate over the input list using a for...of loop.
3. For each number `num` in the list, we check if it is greater than 0 and if its frequency (i.e., the number of times it appears in the list) is greater than or equal to the value of `num` itself. We do this using the `filter` method to count the occurrences of `num` in the list.
4. If the condition is met, we update `max` to be the maximum of `max` and `num`.
5. After iterating over the entire list, we return `max` if it is greater than 0, or -1 if it is not.

Let's test the function with the examples provided:

```
console.log(search([4, 1, 2, 2, 3, 1])); // Output: 2
console.log(search([1, 2, 2, 3, 3, 3, 4, 4, 4])); // Output: 3
console.log(search([5, 5, 4, 4, 4])); // Output: -1
```
The function correctly identifies the greatest integer that meets the condition for each example. If no such value exists, it returns -1.