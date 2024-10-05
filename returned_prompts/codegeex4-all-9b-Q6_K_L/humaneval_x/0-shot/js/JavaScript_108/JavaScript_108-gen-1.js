To solve this problem, we can iterate through each number in the array and calculate the sum of its digits. If the sum is greater than zero, we increment a counter. Finally, we return the counter.

Here's the solution:

```javascript
const countNums = (arr) => {
  let count = 0;
  arr.forEach(num => {
    let sum = 0;
    let digits = num.toString().split('');
    digits.forEach(digit => {
      sum += parseInt(digit);
    });
    if (sum > 0) {
      count++;
    }
  });
  return count;
};
```

We can test the function with the provided test cases:

```javascript
console.log(countNums([])); // 0
console.log(countNums([-1, 11, -11])); // 1
console.log(countNums([1, 1, 2])); // 3
```

The output should be:

```
0
1
3
```