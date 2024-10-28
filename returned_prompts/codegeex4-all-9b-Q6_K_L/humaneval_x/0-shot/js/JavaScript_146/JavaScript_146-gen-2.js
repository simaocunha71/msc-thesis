```javascript
const specialFilter = (nums) => {
  return nums.filter(num => num > 10 && num.toString().charAt(0) % 2 === 1 && num.toString().charAt(num.toString().length - 1) % 2 === 1).length;
}
```
