```js
const sortedListSum = (lst) => {
  const sortedList = lst.filter(word => word.length % 2 === 0).sort((a, b) => a.length - b.length || a.localeCompare(b));
  return sortedList;
}
```
