Here is a JavaScript solution for the problem:

```javascript
const prodSigns = (arr) => {
  if (!arr.length) return null;
  let sign = 1;
  let sum = 0;
  for (let num of arr) {
    if (num === 0) {
      return sum;
    }
    sign *= num > 0 ? 1 : -1;
    sum += Math.abs(num);
  }
  return sign * sum;
};
```

This function first checks if the input array is empty. If it is, it returns null. Otherwise, it initializes two variables: `sign` to 1 and `sum` to 0. It then iterates over the array, updating `sign` based on the sign of each number and adding the absolute value of each number to `sum`. Finally, it returns the product of `sign` and `sum`. If any number in the array is 0, it immediately returns `sum` without updating `sign`. This is because the product of any number and 0 is 0.