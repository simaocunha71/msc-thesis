To determine if it is possible to make all elements in `lst1` even by exchanging elements with `lst2`, we need to check the following:

1. If all elements in `lst1` are already even, return "YES".
2. If there is at least one odd number in `lst1` and at least one even number in `lst2`, return "YES".
3. In all other cases, return "NO".

Here is the implementation of the `exchange` function:

```js
const exchange = (lst1, lst2) => {
  // Check if all elements in lst1 are even
  if (lst1.every(num => num % 2 === 0)) {
    return 'YES';
  }

  // Check if there is at least one odd number in lst1 and at least one even number in lst2
  if (lst1.some(num => num % 2 !== 0) && lst2.some(num => num % 2 === 0)) {
    return 'YES';
  }

  // In all other cases
  return 'NO';
};
```

Let's test the function with the provided examples:

```js
console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])); // "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])); // "NO"
```