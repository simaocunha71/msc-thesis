Here is the solution to the problem:

```javascript
const exchange = (lst1, lst2) => {
  const oddCount = lst1.filter(num => num % 2 !== 0).length;
  const evenCount = lst2.filter(num => num % 2 === 0).length;
  
  return oddCount <= evenCount ? "YES" : "NO";
};
```

In this solution, we first filter the odd numbers from `lst1` and the even numbers from `lst2`, and then compare the counts of these two types of numbers. If the count of odd numbers in `lst1` is less than or equal to the count of even numbers in `lst2`, it means that we can make `lst1` a list of only even numbers by exchanging elements with `lst2`, so we return "YES". Otherwise, we return "NO".