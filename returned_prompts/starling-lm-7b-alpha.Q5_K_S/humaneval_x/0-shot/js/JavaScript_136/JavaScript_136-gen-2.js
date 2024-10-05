Here is a function that solves the problem:

```javascript
const largestSmallestIntegers = (lst) => {
    let a = null;
    let b = null;
    let isNegative = false;
    let isPositive = false;
    for (let i = 0; i < lst.length; i++) {
        if (lst[i] < 0) {
            if (isNegative) {
                a = Math.max(a, lst[i]);
            } else {
                a = lst[i];
                isNegative = true;
            }
        } else if (lst[i] > 0) {
            if (isPositive) {
                b = Math.min(b, lst[i]);
            } else {
                b = lst[i];
                isPositive = true;
            }
        }
    }
    return [a, b];
}
```

The function `largestSmallestIntegers` takes an array `lst` as its parameter. It initial