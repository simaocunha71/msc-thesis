To solve this problem, I will use a for loop to iterate through the list and check if each element is greater than the next one. If it's not, the function will return false. Here's the step-by-step logic:

1. Initialize a boolean variable `isSorted` to `true`.
2. Use a for loop to iterate through the list, starting from index 0 and ending at index `length - 1`.
3. Check if the current element at index `i` is greater than the next element at index `i + 1`. If it's not, set `isSorted` to `false` and break out of the loop.
4. After the loop, check if there are any duplicate values in the list using a for loop. If there are, set `isSorted` to `false`.
5. Finally, return the value of `isSorted`.

Here's the solution in code:

```javascript
const isSorted = (lst) => {
  let isSorted = true;
  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] > lst[i + 1]) {
      isSorted = false;
      break;
    }
  }
  for (let i = 0; i < lst.length; i++) {
    if (lst.indexOf(lst[i]) !== i) {
      isSorted = false;
      break;
    }
  }
  return isSorted;
};
```

This function will return `true` if the list is sorted in ascending order and has no duplicate values. Otherwise, it will return `false`.

To test the function, you can use the following example inputs:

```javascript
console.log(isSorted([5]));       // true
console.log(isSorted([1, 2, 3, 4, 5]));   // true
console.log(isSorted([1, 3, 2, 4, 5]));   // false
console.log(isSorted([1, 2, 3, 4, 5, 6])); // true
console.log(isSorted