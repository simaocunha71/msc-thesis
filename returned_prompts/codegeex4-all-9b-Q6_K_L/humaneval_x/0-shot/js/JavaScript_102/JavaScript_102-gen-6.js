The logic is simple:
  - If x is even, return x
  - If y is even, return y
  - If x is odd and y is odd, return y-1
  - If x is odd and y is even, return y
  - If x is even and y is odd, return y-1
  - If x is even and y is even, return y

Here is the code:

```javascript
const chooseNum = (x, y) => {
    if(x%2 === 0){
        return x;
    } else if (y%2 === 0) {
        return y;
    } else if (x%2 !== 0 && y%2 !== 0) {
        return y-1;
    } else if (x%2 !== 0 && y%2 === 0) {
        return y;
    } else if (x%2 === 0 && y%2 !== 0) {
        return y-1;
    } else if (x%2 === 0 && y%2 === 0) {
        return y;
    }
};
```

Please let me know if you need any further explanation.