```javascript
const getOddCollatz = (n) => {
    if (n === 1) return [1];
    let seq = [n];
    while (n !== 1) {
        if (n % 2 === 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
        if (n !== 1) {
            seq.push(n);
        }
    }
    let oddSeq = seq.filter(x => x % 2 === 1);
    return oddSeq.sort((a, b) => a - b);
};
```
