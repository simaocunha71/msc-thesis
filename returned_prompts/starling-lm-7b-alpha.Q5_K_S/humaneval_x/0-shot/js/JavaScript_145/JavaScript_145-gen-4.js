  const numsSorted = nums.sort((a, b) => {
    const sa = String(a).split('').reduce((s, v) => s + +v, 0);
    const sb = String(b).split('').reduce((s, v) => s + +v, 0);
    return sa === sb ? a - b : sa - sb;
  });

  return numsSorted;
};

*/

This code defines a function called `orderByPoints` which takes an array of integers as an argument. The function uses the `sort` method to sort the array based on a custom comparison function. The comparison function calculates the sum of the digits of each number and compares them. If the sums are equal, the function compares the original indices of the numbers in the array.

Here's how the code works step by step:

1. The `orderByPoints` function takes the `nums` array as an argument.
2. Inside the function, the `nums.sort` method is used to sort the array based on a custom comparison function.
3. The custom comparison function takes two numbers (`a` and `b`) as arguments.
4. Inside the comparison function, the digits of each number are split into an array using the `split` method. The digits are then summed using the `reduce` method, and the sum is stored in the variables `sa` and `sb`.
5. The comparison function returns the result of the comparison between `sa` and `sb`. If the sums are equal, it returns the result of the comparison between `a` and `b`.
6. The `nums.sort` method uses the custom comparison function to sort the array in ascending order based on the sum of the digits of each number.
7. The sorted array is returned as the result of the `orderByPoints` function.

Overall, this code provides a way to sort an array of integers based on the sum of their digits, while maintaining the original order of numbers with the same sum of digits.

To test the function, you can use the provided examples:

```python
>>> orderByPoints([1, 11, -1, -11, -12]) == [-1, -