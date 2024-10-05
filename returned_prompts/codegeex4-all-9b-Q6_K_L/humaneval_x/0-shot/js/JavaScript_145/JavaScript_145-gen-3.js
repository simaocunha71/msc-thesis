```javascript
const orderByPoints = (nums) => {
  return nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, val) => acc + Number(val), 0);
    const sumB = b.toString().split('').reduce((acc, val) => acc + Number(val), 0);
    if (sumA === sumB) {
      return nums.indexOf(a) - nums.indexOf(b);
    }
    return sumA - sumB;
  });
}
```