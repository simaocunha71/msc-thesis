```javascript
const common = (l1, l2) => {
  // Get the unique elements from both lists
  const unique1 = [...new Set(l1)];
  const unique2 = [...new Set(l2)];
  
  // Find the common elements between the two lists
  const commonElements = unique1.filter(item => unique2.includes(item));
  
  // Sort the common elements
  return commonElements.sort((a, b) => a - b);
}
```
