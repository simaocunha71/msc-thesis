Here is the solution using JavaScript:

```javascript
const totalMatch = (lst1, lst2) => {
  const sum1 = lst1.reduce((acc, curr) => acc + curr.length, 0);
  const sum2 = lst2.reduce((acc, curr) => acc + curr.length, 0);
  if (sum1 < sum2) return lst1;
  if (sum1 > sum2) return lst2;
  return lst1;
};
```

In this solution, we use the `reduce()` method to calculate the total number of characters in each list. We then compare these sums to determine which list has fewer characters. If the sums are equal, we return the first list. This solution is case-sensitive and will treat uppercase and lowercase letters as different characters. If you want to ignore case, you can convert all the strings to either lowercase or uppercase before calculating the sums. For example:

```javascript
const totalMatch = (lst1, lst2) => {
  const sum1 = lst1.reduce((acc, curr) => acc + curr.toLowerCase().length, 0);
  const sum2 = lst2.reduce((acc, curr) => acc + curr.toLowerCase().length, 0);
  if (sum1 < sum2) return lst1;
  if (sum1 > sum2) return lst2;
  return lst1;
};
```