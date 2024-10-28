```javascript
const chooseNum = (x, y) => {
  for (let i = y; i >= x; i--) {
    if (i % 2 === 0) {
      return i;
    }
  }
  return -1;
}
```
This solution iterates from the highest number to the lowest number, checking if each number is even. If an even number is found, it is returned. If no even number is found, -1 is returned. This solution has a time complexity of O(n), where n is the difference between the highest and lowest number.