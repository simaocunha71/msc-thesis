Here is the solution in JavaScript:
```javascript
const totalMatch = (lst1, lst2) => {
  const sum1 = lst1.reduce((acc, str) => acc + str.length, 0);
  const sum2 = lst2.reduce((acc, str) => acc + str.length, 0);

  if (sum1 < sum2) return lst1;
  if (sum1 > sum2) return lst2;
  return lst1;
};
```
Here's an explanation of the code:

1. We use the `reduce()` method to calculate the total number of characters in each list. We start with an initial value of 0 and add the length of each string in the list to it.
2. We then compare the sums using conditional statements. If `sum1` is less than `sum2`, we return `lst1`. If `sum1` is greater than `sum2`, we return `lst2`. If the sums are equal, we return `lst1` because the problem statement specifies to return the first list if the sums are equal.
3. The function returns the list with the total number of characters less than the other list, or the first list if the sums are equal.