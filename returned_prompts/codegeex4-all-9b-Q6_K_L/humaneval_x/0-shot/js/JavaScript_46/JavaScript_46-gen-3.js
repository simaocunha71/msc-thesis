```js
const fib4 = (n) => {
  if (n === 0 || n === 1) return 0;
  if (n === 2) return 2;
  if (n === 3) return 0;

  let a = 0;
  let b = 0;
  let c = 2;
  let d = 0;
  let result = 0;

  for (let i = 4; i <= n; i++) {
    result = a + b + c + d;
    a = b;
    b = c;
    c = d;
    d = result;
  }

  return result;
};
```
The function `fib4` calculates the n-th element of the fib4 number sequence using a loop. It initializes the first four elements of the sequence and then iterates from the 5th element up to the n-th element. In each iteration, it calculates the next element by summing up the previous four elements. Finally, it returns the n-th element.