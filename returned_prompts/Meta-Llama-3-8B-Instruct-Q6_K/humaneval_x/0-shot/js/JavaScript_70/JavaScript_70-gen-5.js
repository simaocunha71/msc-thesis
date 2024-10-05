```
const strangeSortList = (lst) => {
  if (lst.length <= 1) return lst;
  const sorted = lst.slice().sort((a, b) => a - b);
  return [
    ...sorted.slice(0, 1),
    ...sorted.slice(-1).slice(0, -1).reverse(),
    ...sorted.slice(1, -1),
  ];
};
```


Explanation:
The function `strangeSortList` takes a list of integers as an argument and returns a new list in the strange order.

1. First, we check if the list has one or zero elements. If it does, we return the list as it is, since there's nothing to sort.

2. We create a copy of the list using `lst.slice()` and sort it in ascending order using `sort()`.

3. We then create a new list by concatenating three parts: 
   - The first element of the sorted list (`sorted.slice(0, 1)`).
   - The last element of the sorted list, but the second last to the end (`sorted.slice(-1).slice(0, -1).reverse()`).
   - The rest of the sorted list, excluding the first and last elements (`sorted.slice(1, -1)`).

4. We return the new list.

This function works by alternating between the smallest and largest elements, effectively "zigzagging" through the list. This is what creates the "strange" order.