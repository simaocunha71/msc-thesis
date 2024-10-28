Here is the solution to the problem:

```javascript
const totalMatch = (lst1, lst2) => {
  let sum1 = 0, sum2 = 0;
  for (let str of lst1) {
    sum1 += str.length;
  }
  for (let str of lst2) {
    sum2 += str.length;
  }
  if (sum1 < sum2) {
    return lst1;
  } else if (sum1 > sum2) {
    return lst2;
  } else {
    return lst1;
  }
};
```



Explanation:

1. Initialize two variables `sum1` and `sum2` to keep track of the total number of characters in each list.
2. Loop through each string in `lst1` and add its length to `sum1`.
3. Loop through each string in `lst2` and add its length to `sum2`.
4. Compare `sum1` and `sum2`. If `sum1` is less than `sum2`, return `lst1`. If `sum2` is less than `sum1`, return `lst2`.
5. If `sum1` is equal to `sum2`, return `lst1` as per the problem statement.

This solution has a time complexity of O(n), where n is the total number of strings in both lists. It iterates through each string in both lists once to calculate the total number of characters. The space complexity is O(1), as it only uses a constant amount of space to store the sums.