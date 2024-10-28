```javascript
const moveOneBall = (arr) => {
    if (!arr.length) return true;
    let max = Math.max(...arr);
    let count = 0;
    while (arr[0] !== max) {
        arr.push(arr.shift());
        count++;
    }
    return count <= arr.length;
};
```