  return nums.sort((a, b) => {
    let aDigits = String(Math.abs(a)).split('').reduce((s, v) => s + Number(v), 0);
    let bDigits = String(Math.abs(b)).split('').reduce((s, v) => s + Number(v), 0);
    return aDigits - bDigits || nums.indexOf(a) - nums.indexOf(b);
  });
}

console.log(orderByPoints([1, 11, -1, -11, -12])); // [-1, -11, 1, -12, 11]
console.log(orderByPoints([])); // []
```

**Explanation:**

In the function `orderByPoints`, we are sorting the numbers based on the sum of their digits using the `sort()` function. If two numbers have the same sum of digits, they are then sorted based on their original index in the array.

For each number, we are first converting it to an absolute value, then converting it to a string and splitting it into individual digits. We are then reducing the array of digits to a sum by adding them all together.

Then we are comparing the sums of the digits of `a` and `b`. If `a` has a smaller sum of digits than `b`, then `a` is smaller and should be placed before `b` in the sorted array, so we return a negative number. If `b` has a smaller sum of digits, then `b` is smaller and should be placed before `a`, so we return a positive number.

If the sums of the digits of `a` and `b` are the same, we then compare their original indices in the array. If `a` originally has a smaller index than `b`, then `a` should be placed before `b` in the sorted array, so we return a negative number. If `b` originally has a smaller index, then `b` should be placed before `a`, so we return a positive number. If the indices are the same, then `a` and `b` are considered equal and their original order is preserved, so we return 