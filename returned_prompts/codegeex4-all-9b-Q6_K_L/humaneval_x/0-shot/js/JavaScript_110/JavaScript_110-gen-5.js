```js
const exchange = (lst1, lst2) => {
  var even = lst1.filter(x => x % 2 === 0);
  var odd = lst2.filter(x => x % 2 !== 0);
  if (even.length === lst1.length) return 'YES';
  if (odd.length >= lst1.length - even.length) return 'YES';
  return 'NO';
}
```
