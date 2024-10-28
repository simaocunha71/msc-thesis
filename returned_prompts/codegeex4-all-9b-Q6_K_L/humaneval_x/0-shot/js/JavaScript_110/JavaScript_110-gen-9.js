```javascript
const exchange = (lst1, lst2) => {
  let numOdds = lst1.filter(x => x % 2).length;
  let numEvens = lst2.filter(x => x % 2 === 0).length;
  return numOdds <= numEvens ? 'YES' : 'NO';
}
```