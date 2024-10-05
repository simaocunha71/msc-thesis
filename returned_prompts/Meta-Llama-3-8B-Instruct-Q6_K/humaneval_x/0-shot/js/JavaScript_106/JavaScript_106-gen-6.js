```javascript
const f = (n) => {
  return Array.from({ length: n }, (v, i) => i % 2 === 0 ? factorial(i) : i * (i + 1) / 2);
};

const factorial = (n) => {
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
};

console.log(f(5)); // [1, 2, 6, 24, 15]
```

Each of these functions does the same thing: they take an integer `n` as an argument and return a list of size `n`. The value of the element at index `i` in the list is the factorial