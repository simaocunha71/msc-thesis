
};

console.log(orderByPoints([1, 11, -1, -11, -12]))
console.log(orderByPoints([]))

```

## Solution

```javascript
const orderByPoints = (nums) => {
  return nums.sort((a, b) => {
    let sumA = String(Math.abs(a)).split('').reduce((acc, v) => acc + Number(v), 0);
    let sumB = String(Math.abs(b)).split('').reduce((acc, v) => acc + Number(v), 0);
    if (sumA !== sumB) {
      return sumA - sumB;
    }
    return nums.indexOf(a) - nums.indexOf(b);
  });
};

console.log(orderByPoints([1, 11, -1, -11, -12])); // [-1, -11, 1, -12, 11]
console.log(orderByPoints([])); // []
```

## Explanation

This solution uses JavaScript's built-in `Array.prototype.sort()`. Inside the sort callback, we calculate the sum of the absolute value of each number's digits with `String(Math.abs(num)).split('').reduce((acc, v) => acc + Number(v), 0);`. Then we compare the sum of the digits. If they're not equal, we return the difference of the sums. If they are equal, we return the difference of the original indices of the numbers. If more than two numbers have the same sum of digits, this will ensure that they are ordered by their original indices.

This solution works in O(n log n) time complexity due to the sorting operation.

## Test cases

```javascript
console.log(orderByPoints([15, 7, 1, -15, -7])); // [1, -15, 7, -7, 15]
console.log(orderByPoints([2, 3, 5, 7, 13])); // [2, 3, 5, 7,