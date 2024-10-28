```javascript
const orderByPoints = (nums) => {
  return nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, curr) => acc + Math.abs(+curr), 0);
    const sumB = b.toString().split('').reduce((acc, curr) => acc + Math.abs(+curr), 0);
    return sumA - sumB;
  });
};
```