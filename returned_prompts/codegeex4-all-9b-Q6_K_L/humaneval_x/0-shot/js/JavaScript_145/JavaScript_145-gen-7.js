```javascript
const orderByPoints = (nums) => {
  return nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, val) => acc + Math.abs(parseInt(val)), 0);
    const sumB = b.toString().split('').reduce((acc, val) => acc + Math.abs(parseInt(val)), 0);
    return sumA - sumB;
  });
}
```
