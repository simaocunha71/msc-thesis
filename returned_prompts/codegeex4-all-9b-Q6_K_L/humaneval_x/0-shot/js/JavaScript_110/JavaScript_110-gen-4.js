```js
const exchange = (lst1, lst2) => {
  const evenNumbers = lst2.filter(num => num % 2 === 0);
  return evenNumbers.length >= lst1.length - lst1.filter(num => num % 2 === 0).length ? 'YES' : 'NO';
}
```
