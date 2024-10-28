```
const iscube = (a) => {
  if (a < 0) {
    a = -a;
  }
  const c = Math.cbrt(a);
  return c === Math.round(c);
};
```


This function first makes sure that the input is non-negative by taking the absolute value of the input. Then it calculates the cube root of the input using the `Math.cbrt()` function. Finally, it checks if the cube root is an integer by comparing it to its rounded value. If the two values are equal, the input is a perfect cube and the function returns `true`. Otherwise, it returns `false`.