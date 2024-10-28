```js
const f = (n) => {
  let result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      result.push(factorial(i));
    } else {
      result.push(sumToI(i));
    }
  }
  return result;
};

const factorial = (n) => {
  let result = 1;
  for (let i = 1; i <= n; i++) {
    result *= i;
  }
  return result;
};

const sumToI = (n) => {
  let result = 0;
  for (let i = 1; i <= n; i++) {
    result += i;
  }
  return result;
};
```