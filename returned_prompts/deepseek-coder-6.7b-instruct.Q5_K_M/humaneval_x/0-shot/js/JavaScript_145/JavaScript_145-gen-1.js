  return nums.sort((a, b) => {
    const sumA = String(Math.abs(a)).split('').reduce((acc, v) => acc + parseInt(v), 0)
    const sumB = String(Math.abs(b)).split('').reduce((acc, v) => acc + parseInt(v), 0)
    return sumA - sumB || nums.indexOf(a) - nums.indexOf(b)
  })
}
```

## Solution: 

This solution uses the JavaScript `Array.prototype.sort()` function to sort the array. The `sort()` function sorts the elements of an array in place and returns the array. The default sort order is built upon converting the elements into strings, then comparing their sequences of UTF-16 code unit values.

In this case, we provide a custom comparison function to `sort()`. This function takes two arguments, `a` and `b`, which are the elements being compared in the array.

In the custom comparison function, we calculate the sum of the digits of `a` and `b` by converting them to strings, splitting them into an array of characters, mapping each character to its integer value with `parseInt()`, and reducing the array to the sum with `reduce()`.

If the sums of the digits of `a` and `b` are not equal, the function returns the difference of the sums. This will determine the sort order of the elements.

If the sums of the digits of `a` and `b` are equal, the function returns the difference of the original indices of `a` and `b` in the original array. This will determine the sort order of the elements when the sums are equal.

Finally, the function returns the sorted array.

Note: The `Math.abs()` function is used to ensure that negative numbers are handled correctly.

## Test Case:
```js
console.log(orderByPoints([1, 11, -1, -11, -12]))  // [-1, -11, 1, -12, 11]
console.log(orderByPoints([]))  // []
```

## Time complexity: 
The time complexity of this solution