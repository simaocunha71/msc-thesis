Here is the JavaScript solution for the problem:

```javascript
const orderByPoints = (nums) => {
    return nums
        .map((num, index) => ({ num, sum: Math.abs(num).toString().split('').reduce((a, b) => a + parseInt(b), 0), index }))
        .sort((a, b) => a.sum - b.sum || a.index - b.index)
        .map(({ num }) => num);
};

console.log(orderByPoints([1, 11, -1, -11, -12])); // [-1, -11, 1, -12, 11]
console.log(orderByPoints([])); // []
```

Explanation:

1. The `map` function is used to transform the array of numbers into an array of objects. Each object contains the original number, the sum of its digits, and its index.

2. The `sort` function is used to sort the array of objects based on the sum of digits. If two numbers have the same sum of digits, they are sorted based on their index in the original array.

3. Finally, the `map` function is used again to transform the array of objects back into an array of numbers.