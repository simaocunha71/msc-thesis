The function should return the list with the total number of characters in all strings less than the other list. If the two lists have the same number of characters, it should return the first list.

Here is the JavaScript solution for the problem:

```javascript
const totalMatch = (lst1, lst2) => {
  const total1 = lst1.reduce((acc, current) => acc + current.length, 0);
  const total2 = lst2.reduce((acc, current) => acc + current.length, 0);
  
  if (total1 < total2) {
    return lst1;
  } else if (total1 > total2) {
    return lst2;
  } else {
    return lst1;
  }
};
```

This function uses the `reduce` method to calculate the total number of characters in each list. It then compares these totals and returns the list with the smaller total. If the totals are equal, it returns the first list. This function should work correctly for all the examples provided.