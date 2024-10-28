To solve this problem, you can follow these steps:

1. Define a function called `sortEven` that takes a list `l` as an argument.
2. Create a new list `l'` to store the sorted even values.
3. Iterate through the elements of `l` using the `for...of` loop.
4. Check if the index of the current element is even using the modulo operator `%`.
5. If the index is even, push the current element to the `l'` list using the `push()` method.
6. If the index is odd, sort the `l'` list using the `sort()` method.
7. Return the `l'` list.
8. Test the function with example inputs to verify its correctness.

Here's the complete code:

```javascript
const sortEven = (l) => {
  let l' = [];
  for (const elem of l) {
    if (l.indexOf(elem) % 2 === 0) {
      l'.push(elem);
    } else {
      l' = l'.sort();
    }
  }
  return l';
};

console.log(sortEven([1, 2, 3])); // [1, 2, 3]
console.log(sortEven([5, 6, 3, 4])); // [3, 6, 5, 4]
```

This implementation sorts only the even values in the list, while keeping the odd values unchanged. The `sort()` method is used to sort the even values in ascending order.

Please note that the `sort()` method sorts the elements in place and returns the sorted list.

I hope this helps! Let me know if you have any more questions.

Best,
Andy

P.S. As an additional exercise, you can try modifying the function to handle nested lists as well.

Here's an updated version of the function that supports nested lists:

```javascript
const sortEven = (l) => {
  const flatten = (list) => list.reduce((acc, curr) => Array.isArray(curr) ? [...acc, ...flatten(curr)] : [...acc, curr], []);