  if (n === 0) return 0;
  if (n === 1) return 0;
  if (n === 2) return 2;
  if (n === 3) return 0;

  let fib = [0, 0, 2, 0];

  for(let i = 4; i <= n; i++){
    fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4];
  }

  return fib[n];
};

console.log(fib4(5)); // 4
console.log(fib4(6)); // 8
console.log(fib4(7)); // 14

```


## 5. 6 kyu - Double Sort

