```javascript
const maximum = (arr, k) => {
    const sortedArr = arr.sort((a, b) => b - a);
    const result = [];
    for (let i = 0; i < k; i++) {
        result.push(sortedArr[i]);
    }
    return result;
};
```