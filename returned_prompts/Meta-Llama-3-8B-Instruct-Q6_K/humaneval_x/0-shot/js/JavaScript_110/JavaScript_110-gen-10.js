Here is the solution:

```javascript
const exchange = (lst1, lst2) => {
  let count = 0;
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 !== 0) {
      for (let j = 0; j < lst2.length; j++) {
        if (lst2[j] % 2 === 0) {
          lst1[i] = lst2[j];
          lst2[j] = undefined;
          count++;
          break;
        }
      }
    }
  }
  return count < lst1.length ? "NO" : "YES";
};
```

This function works by iterating through lst1 and checking if each element is odd. If it is, it iterates through lst2 to find the first even element and swaps it with the odd element in lst1. It keeps track of the number of swaps it makes. If it makes as many swaps as there are odd numbers in lst1, it returns "YES". Otherwise, it returns "NO". This ensures that it only returns "YES" if it is possible to make all the elements in lst1 even by exchanging them with elements in lst2.