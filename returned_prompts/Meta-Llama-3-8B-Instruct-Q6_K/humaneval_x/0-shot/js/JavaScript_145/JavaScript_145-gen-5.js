Here is the solution to the problem:

```javascript
const orderByPoints = (nums) => {
  return nums.sort((a, b) => {
    if (a < 0) {
      a = a.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    } else {
      a = a.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    }
    if (b < 0) {
      b = b.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    } else {
      b = b.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    }
    if (a === b) {
      return nums.indexOf(a) - nums.indexOf(b);
    } else {
      return a - b;
    }
  });
};
```


This function works by first calculating the sum of the digits of each number in the input list. It does this by converting each number to a string, splitting it into individual digits, and then summing up the digits. This sum is then used to sort the list.

If two numbers have the same sum of digits, the function uses the original index of the numbers in the list to determine the order. This is done by subtracting the index of the first number from the index of the second number. If the first number has a smaller index, the function returns a negative number, which causes the first number to come before the second number in the sorted list. If the second number has a smaller index, the function returns a positive number, which causes the second number to come before the first number in the sorted list. If the two numbers have the same index, the function returns 0, which means that the order of the numbers is not changed.

The function uses the built-in `sort` method of the list, which sorts the list in place. The `sort` method takes a compare function as an argument, which is used to determine the order of the elements in the list. In this case, the compare function is defined as a lambda function that takes two arguments, `a` and `b`, and returns a value that determines the order of `a` and `b`. The value returned by the compare function is used to sort the list.

The function returns the sorted list. If the input list is empty, the function returns an empty list. If the input list contains only one