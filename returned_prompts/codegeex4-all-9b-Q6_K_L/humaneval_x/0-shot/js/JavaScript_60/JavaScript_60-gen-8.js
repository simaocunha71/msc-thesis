```js
const sumToN = (n) => {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}
```

B:
```js
const sumToN = (n) => {
  return n * (n + 1) / 2;
}
```

C:
```js
const sumToN = (n) => {
  return n + 1;
}
```

D:
```js
const sumToN = (n) => {
  return n * n;
}
```

E:
```js
const sumToN = (n) => {
  return n / 2;
}
```

F:
```js
const sumToN = (n) => {
  return n * n * n;
}
```