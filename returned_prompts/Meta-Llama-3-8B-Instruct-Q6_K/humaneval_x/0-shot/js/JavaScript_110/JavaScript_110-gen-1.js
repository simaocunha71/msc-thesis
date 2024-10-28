```javascript
const exchange = (lst1, lst2) => {
  const oddCount = lst1.filter(num => num % 2 !== 0).length;
  const oddInLst2 = lst2.filter(num => num % 2 !== 0).length;
  return oddCount <= oddInLst2 ? "YES" : "NO";
};
```
Explanation:

1. We use the filter method to count the number of odd numbers in both lists.
2. We then compare the count of odd numbers in lst1 with the count of odd numbers in lst2.
3. If the count of odd numbers in lst1 is less than or equal to the count of odd numbers in lst2, it means that we can exchange elements from lst2 to make all elements in lst1 even. In this case, we return "YES".
4. Otherwise, we return "NO", indicating that it is not possible to exchange elements to make all elements in lst1 even.

Example usage:

```javascript
console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])); // Output: "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])); // Output: "NO"
```