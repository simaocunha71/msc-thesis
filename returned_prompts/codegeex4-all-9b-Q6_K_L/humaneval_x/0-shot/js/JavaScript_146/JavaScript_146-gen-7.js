```javascript
const specialFilter = (nums) => {
  const isOdd = (num) => {
    const str = num.toString();
    return str[0] % 2 !== 0 && str[str.length - 1] % 2 !== 0;
  };
  return nums.filter((num) => num > 10 && isOdd(num)).length;
};
```