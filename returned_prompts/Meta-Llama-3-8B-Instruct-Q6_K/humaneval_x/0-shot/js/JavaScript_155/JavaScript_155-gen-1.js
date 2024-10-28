```javascript
const evenOddCount = (num) => {
    let evenCount = 0;
    let oddCount = 0;
    let numStr = Math.abs(num).toString();

    for (let char of numStr) {
        if (+char % 2 === 0) {
            evenCount++;
        } else {
            oddCount++;
        }
    }
    return [evenCount, oddCount];
};
``` 