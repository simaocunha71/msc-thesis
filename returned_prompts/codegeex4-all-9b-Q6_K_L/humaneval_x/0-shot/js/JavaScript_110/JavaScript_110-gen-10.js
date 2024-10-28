```js
const exchange = (lst1, lst2) => {
  // Check if all elements in lst1 are even
  if (lst1.every(num => num % 2 === 0)) {
    return "YES";
  }
  // Check if there is at least one even number in lst2
  if (lst2.some(num => num % 2 === 0)) {
    return "YES";
  }
  // If neither of the above conditions are met, return "NO"
  return "NO";
}
```
