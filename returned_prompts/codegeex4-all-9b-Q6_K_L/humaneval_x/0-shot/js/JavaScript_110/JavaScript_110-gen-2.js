To determine if it's possible to make all elements of `lst1` even by exchanging elements with `lst2`, we need to check if there are enough even numbers in `lst2` to exchange with the odd numbers in `lst1`.

Here's a step-by-step breakdown of the solution:

1. Count the number of odd numbers in `lst1` using the `filter()` method.
2. Count the number of even numbers in `lst2` using the `filter()` method.
3. If the count of odd numbers in `lst1` is less than or equal to the count of even numbers in `lst2`, return "YES". Otherwise, return "NO".

Here's the implementation of the `exchange()` function:

```javascript
const exchange = (lst1, lst2) => {
  const oddCount = lst1.filter(x => x % 2 !== 0).length;
  const evenCount = lst2.filter(x => x % 2 === 0).length;

  return oddCount <= evenCount ? 'YES' : 'NO';
};
```

Here's how it works:

1. The `filter()` method creates a new array with all elements that pass the test implemented by the provided function. In this case, we're filtering `lst1` for odd numbers and `lst2` for even numbers.
2. The `length` property is used to count the number of elements in the filtered arrays.
3. The comparison `oddCount <= evenCount` checks if there are enough even numbers in `lst2` to exchange with the odd numbers in `lst1`.
4. The function returns "YES" if the condition is met, otherwise it returns "NO".

This solution assumes that the input lists will be non-empty, as stated in the problem.