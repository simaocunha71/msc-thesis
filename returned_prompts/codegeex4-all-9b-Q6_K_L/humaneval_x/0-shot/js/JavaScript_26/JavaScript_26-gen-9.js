```javascript
const removeDuplicates = (numbers) => {
  const count = {};
  const result = [];
  numbers.forEach((num) => {
    if (!count[num]) {
      count[num] = 1;
      result.push(num);
    }
  });
  return result;
};
```