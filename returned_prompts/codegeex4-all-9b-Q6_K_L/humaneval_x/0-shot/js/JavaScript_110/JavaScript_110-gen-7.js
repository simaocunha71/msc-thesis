To determine whether it is possible to exchange elements between `lst1` and `lst2` to make all elements of `lst1` even, we can follow these steps:

1. Count the number of even and odd numbers in `lst1`.
2. Count the number of even numbers in `lst2`.
3. If the number of even numbers in `lst1` plus the number of even numbers in `lst2` is equal to the length of `lst1`, then it is possible to make all elements of `lst1` even through exchanges. Otherwise, it is not possible.
4. If the number of odd numbers in `lst1` is greater than the number of even numbers in `lst2`, then it is not possible to make all elements of `lst1` even through exchanges. Otherwise, it is possible.

Here is the implementation of the `exchange` function:

```javascript
const exchange = (lst1, lst2) => {
  const countEvens = (arr) => arr.filter(num => num % 2 === 0).length;
  const countOdds = (arr) => arr.filter(num => num % 2 !== 0).length;

  const evensInLst1 = countEvens(lst1);
  const evensInLst2 = countEvens(lst2);
  const oddsInLst1 = countOdds(lst1);

  if (evensInLst1 + evensInLst2 >= lst1.length && oddsInLst1 <= evensInLst2) {
    return 'YES';
  } else {
    return 'NO';
  }
};
```

Let's test the function with the provided examples:

```javascript
console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])); // "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])); // "NO"
```

The function returns the expected results.