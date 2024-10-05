Here is the JavaScript solution for the problem:

```javascript
const cycpatternCheck = (a, b) => {
    if (b.length > a.length) {
        return false;
    }
    for (let i = 0; i < a.length - b.length + 1; i++) {
        let temp = a.slice(i, i + b.length);
        for (let j = 0; j < b.length; j++) {
            if (temp[j] !== b[j]) {
                break;
            }
            if (j === b.length - 1) {
                return true;
            }
        }
        temp = temp.slice(1) + temp[0];
    }
    return false;
}
```

This solution works by checking each possible substring of length `b.length` in `a`, and then checking if that substring is a rotation of `b`. If it is, it returns `true`. If it goes through all possible substrings without finding a match, it returns `false`.