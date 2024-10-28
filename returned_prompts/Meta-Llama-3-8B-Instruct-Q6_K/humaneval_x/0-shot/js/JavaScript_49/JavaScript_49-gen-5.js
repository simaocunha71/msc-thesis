```javascript
const modp = (n, p) => {
    if (n === 0) return 1;
    let result = 1;
    n = n % p;
    while (n > 0) {
        if (n % 2 === 1) {
            result = (result * n) % p;
        }
        n = Math.floor(n / 2);
    }
    return result;
};
``` 