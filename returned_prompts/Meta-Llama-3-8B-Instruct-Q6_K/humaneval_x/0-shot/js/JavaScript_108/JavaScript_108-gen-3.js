Here is a JavaScript function that counts the number of elements in the array that have a sum of digits greater than 0:

```javascript
const countNums = (arr) => {
  return arr.filter(num => {
    let sum = 0;
    const str = num.toString();
    for (let i = 0; i < str.length; i++) {
      const digit = parseInt(str[i]);
      sum += digit;
    }
    return sum > 0;
  }).length;
};
```

This function works by first converting each number in the array to a string, then iterating over each character in the string to extract the digits. It calculates the sum of these digits, and if the sum is greater than 0, it includes the number in the count. Finally, it returns the length of the filtered array, which is the number of elements that have a sum of digits greater than 0.