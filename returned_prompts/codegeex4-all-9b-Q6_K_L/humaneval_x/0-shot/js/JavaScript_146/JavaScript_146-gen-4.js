```javascript
const specialFilter = (nums) => {
    return nums.filter(num => num > 10 && num.toString()[0] % 2 === 1 && num.toString().slice(-1) % 2 === 1).length;
}
```
