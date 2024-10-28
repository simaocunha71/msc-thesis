```js
const orderByPoints = (nums) => {
    const sumDigits = (num) => {
        return Math.abs(num).toString().split('').reduce((a, b) => a + Number(b), 0);
    };
    return nums.sort((a, b) => {
        const sumA = sumDigits(a);
        const sumB = sumDigits(b);
        if (sumA === sumB) {
            return nums.indexOf(a) - nums.indexOf(b);
        }
        return sumA - sumB;
    });
};
```
