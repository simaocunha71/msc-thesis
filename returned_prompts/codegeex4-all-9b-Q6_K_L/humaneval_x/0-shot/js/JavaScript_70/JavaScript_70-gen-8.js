You can solve this problem by using a loop that iterates over the list and adds the minimum or maximum value of the remaining list to a new list.

Here is the implementation in JavaScript:

```javascript
const strangeSortList = (lst) => {
  let res = [];
  while (lst.length > 0) {
    if (res.length % 2 === 0) {
      res.push(Math.min(...lst));
    } else {
      res.push(Math.max(...lst));
    }
    lst.splice(lst.indexOf(res[res.length - 1]), 1);
  }
  return res;
}
```

In this code:

- We initialize an empty list `res` to store the sorted elements.
- We then enter a loop that continues until the input list `lst` is empty.
- Inside the loop, we check whether the length of `res` is even or odd using the modulus operator `%`. If it's even, we add the minimum value of the remaining list to `res` using the `Math.min()` function. If it's odd, we add the maximum value of the remaining list to `res` using the `Math.max()` function.
- We then remove the added element from the input list `lst` using the `splice()` function.
- Finally, we return the sorted list `res`.