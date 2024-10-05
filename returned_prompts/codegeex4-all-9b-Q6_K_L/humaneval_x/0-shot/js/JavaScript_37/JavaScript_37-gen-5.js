```javascript
const sortEven = (l) => {
  // Extract the even-indexed elements
  const evenIndexed = l.filter((_, i) => i % 2 === 0);
  // Sort the even-indexed elements
  evenIndexed.sort((a, b) => a - b);
  // Replace the even-indexed elements with the sorted ones
  return l.map((_, i) => (i % 2 === 0 ? evenIndexed[i / 2] : l[i]));
}
```