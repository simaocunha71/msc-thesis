  const f 		= (x) => poly(xs, x);
  const df 		= (x) => {
    let h = 0.00001;
    return (f(x + h) - f(x)) / h;
  };
  const n = xs.length;
  const newton = (x) => x - f(x) / df(x);

  let x = n / 2.0;
  for (let i = 0; i < 100; i++) {
    x = newton(x);
  }
  return x;
}

const {poly, findZero}
```

## 1.8.2. 함수의 수정

```javascript
