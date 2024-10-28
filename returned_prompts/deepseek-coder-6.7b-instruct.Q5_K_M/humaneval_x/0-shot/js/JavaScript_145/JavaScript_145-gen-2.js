  return nums.sort((a, b) => {
    const sumA = String(Math.abs(a)).split('').reduce((acc, cur) => acc + +cur, 0);
    const sumB = String(Math.abs(b)).split('').reduce((acc, cur)=>  acc + +cur, 0);

    if (sumA !== sumB) {
      return sumA - sumB;
    } else {
      return nums.indexOf(a) - nums.indexOf(b);
    }
  });
};

console.log(orderByPoints([1, 11, -1, -11, -12]));
console.log(orderByPoints([]));
```

## Answer:
This function sorts an array of integers in ascending order based on the sum of their digits. If two integers have the same sum of digits, they are sorted based on their index in the original array.

```javascript
const orderByPoints 
= (nums) => {
  return nums.sort((a, b) => {
    const sumA = String(Math.abs(a)).split('').reduce((acc, cur) => acc + +cur, 0);
    const sumB = String(Math.abs(b)).split('').reduce((acc, cur)=>  acc + +cur, 0);

    if (sumA !==