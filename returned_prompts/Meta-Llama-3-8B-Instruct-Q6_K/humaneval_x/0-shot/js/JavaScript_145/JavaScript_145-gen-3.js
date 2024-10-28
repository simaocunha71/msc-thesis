Here is the solution in JavaScript:
```
const orderByPoints = (nums) => {
  return nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);
    const sumB = b.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);
    if (sumA === sumB) {
      return nums.indexOf(a) - nums.indexOf(b);
    }
    return sumA - sumB;
  });
};
```
Here's an explanation of the solution:

1. We use the `sort()` method to sort the array.
2. We define a compare function that takes two elements `a` and `b` as arguments.
3. We calculate the sum of the digits of each element using the `toString()`, `split('')`, and `reduce()` methods.
4. If the sums are equal, we use the `indexOf()` method to determine the order based on the original index of the elements in the array.
5. If the sums are not equal, we return the difference between the sums.

You can test this function with the examples you provided:
```
console.log(orderByPoints([1, 11, -1, -11, -12])); // [-1, -11, 1, -12, 11]
console.log(orderByPoints([])); // []
```
I hope this helps! Let me know if you have any questions. 😊

---

Note: This solution assumes that the input array only contains integers. If the array can contain other types of values, additional checks may be necessary.