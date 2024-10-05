  return nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, cur) => acc + Math.abs(parseInt(cur)), 0);
    const sumB = b.toString().split('').reduce((acc, cur) => acc + Math.abs(parseInt(cur)), 0);
    return sumA - sumB || nums.indexOf(a) - nums.indexOf(b);
  });
}

orderByPoints([1, 11, -1, -11, -12]) //== [-1, -11, 1, -12, 11]
orderByPoints([]) //== []
```


### Code Explanation:

This code takes a list of numbers and sorts them first by the sum of their digits, and then by their original position in the list if the sums are equal.

The built-in `sort` function in JavaScript is used to sort the numbers. The `sort` function takes a comparator function as its argument which defines the sort order.

For each pair of numbers (a, b), the comparator function first calculates the sum of the digits for `a` and `b`. If the sums are different, it returns `sumA - sumB` which tells JavaScript's sort function to sort `a` before `b` if `sumA` is smaller than `sumB`, and to sort `b` before `a` if `sumA` is larger than `sumB`. If the sums are equal, it returns `nums.indexOf(a) - nums.indexOf(b)` which tells JavaScript's sort function to sort `a` before `b` if its original position in the list is smaller than `b`'s, and to sort `b` before `a` if its original position in the list is larger than `b`'s.

In the end, the `sort` function returns the sorted list.

This code is efficient because it calculates the sum of the digits and the original position of each number only once for each pair of numbers, and uses the built-in `sort` function which is usually implemented in such a way that it sorts the numbers in-place and in linear time,