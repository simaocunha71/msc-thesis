```javascript
const exchange = (lst1, lst2) => {
  let count = 0;
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 !== 0) {
      for (let j = 0; j < lst2.length; j++) {
        if (lst2[j] % 2 === 0) {
          lst1[i] = lst2[j];
          lst2[j] = lst1[i];
          count++;
          break;
        }
      }
    }
  }
  return count === lst1.length - lst1.filter(num => num % 2 !== 0).length ? "YES" : "NO";
};
```

Explanation:

*   We initialize a count variable to keep track of the number of exchanges made.
*   We iterate through lst1 and check if each element is odd (i.e., not divisible by 2).
*   If an element is odd, we iterate through lst2 to find the first even element and swap them.
*   We increment the count variable each time an exchange is made.
*   After all exchanges, we check if the count is equal to the number of odd elements in lst1. If it is, it means all elements in lst1 can be made even by exchanging elements with lst2, so we return "YES". Otherwise, we return "NO".