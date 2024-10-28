Here is the solution:

```javascript
const exchange = (lst1, lst2) => {
  let oddCount = 0;
  for (let num of lst1) {
    if (num % 2 !== 0) {
      oddCount++;
    }
  }
  if (oddCount > lst2.length) {
    return "NO";
  }
  return "YES";
};
```

In this solution, we first count the number of odd elements in `lst1`. If the count is greater than the length of `lst2`, it is not possible to make all elements of `lst1` even by exchanging elements with `lst2`, so we return "NO". Otherwise, we return "YES". This solution has a time complexity of O(n), where n is the length of `lst1`. The space complexity is O(1), as we only use a constant amount of space to store the count of odd elements.