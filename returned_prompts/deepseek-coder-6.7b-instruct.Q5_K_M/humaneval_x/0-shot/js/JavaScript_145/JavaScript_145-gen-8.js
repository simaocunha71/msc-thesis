  const getSum = (num) => {
    return num.toString().split('').reduce((acc, cur) => {
      return acc + Math.abs(parseInt(cur));
    }, 0);
  };

  return nums.sort((a, b) => {
    const diff = getSum(a) - getSum(b);
    if (diff === 0) {
      return nums.indexOf(a) - nums.indexOf(b);
    }
    return diff;
  });
};

console.log(orderByPoints([1, 11, -1, -11, -12])) //[-1, -11, 1, -12, 11]
console.log(orderByPoints([])) // []

```

Explanation:
In the function `orderByPoints(nums)`, we first define a helper function `getSum(num)` which returns the sum of the digits of a number.
We then use the `sort()` method on the given array of numbers. The `sort()` method sorts the elements of an array in place and returns the array. The default sort order is built upon converting the elements into strings, then comparing their sequences of UTF-16 code unit values. We override this default behaviour by providing a comparison function.
In the comparison function, we first calculate the difference in sum of digits of the two numbers `a` and `b`. If the difference is 0, we consider the original index of the numbers in the list to determine their order.

**Complexity Analysis:**
- The time complexity of the solution is O(nlogn), where n is the length of the list. This is because we are sorting the list, which takes O(nlogn) time.
- The space complexity is O(n), where n is the length of the list. This is because we are storing the list in memory.


This solution assumes that all inputs are valid integers. If the inputs can be floating-point numbers or other types of values, the solution would need to be adjusted accordingly.

*/

































