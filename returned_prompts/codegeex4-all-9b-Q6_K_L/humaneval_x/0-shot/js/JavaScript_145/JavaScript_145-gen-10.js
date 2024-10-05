```js
const orderByPoints = (nums) => {
  return nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, num) => acc + Math.abs(num), 0);
    const sumB = b.toString().split('').reduce((acc, num) => acc + Math.abs(num), 0);
    if (sumA === sumB) {
      return nums.indexOf(a) - nums.indexOf(b);
    }
    return sumA - sumB;
  });
};
```