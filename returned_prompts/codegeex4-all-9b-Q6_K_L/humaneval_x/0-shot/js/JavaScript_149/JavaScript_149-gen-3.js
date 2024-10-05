```javascript
const sortedListSum = (lst) => {
  const filtered = lst.filter(word => word.length % 2 === 0);
  const sorted = filtered.sort((a, b) => {
    if (a.length === b.length) {
      return a.localeCompare(b);
    }
    return a.length - b.length;
  });
  return sorted;
}
```
