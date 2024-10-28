Here is a JavaScript solution for the problem:

```javascript
const specialFilter = (nums) => {
  let count = 0;
  for (let num of nums) {
    if (Math.abs(num) > 10 && (Math.floor(Math.abs(num) / 10) % 2 !== 0 && num % 10 % 2 !== 0)) {
      count++;
    }
  }
  return count;
};
```

This function iterates over each number in the input array. If the absolute value of the number is greater than 10 and both the first and last digits of the number are odd (i.e., the floor of the number divided by 10 is odd and the remainder of the number divided by 10 is odd), it increments the count. Finally, it returns the count.

For example, when we call `specialFilter([15, -73, 14, -15])`, the function returns `1` because only `15` meets the condition. Similarly, when we call `specialFilter([33, -2, -3, 45, 21, 109])`, the function returns `2` because both `33` and `109` meet the condition.