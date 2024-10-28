```js
const getOddCollatz = (n) => {
  let arr = [];
  while (n !== 1) {
    if (n % 2 === 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
      arr.push(n);
    }
  }
  arr.push(1);
  return arr;
};
```

B:
```js
const getOddCollatz = (n) => {
  let arr = [];
  while (n !== 1) {
    if (n % 2 === 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
      arr.push(n);
    }
  }
  arr.push(1);
  return arr.sort((a, b) => a - b);
};
```

C:
```js
const getOddCollatz = (n) => {
  let arr = [];
  while (n !== 1) {
    if (n % 2 === 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
      arr.push(n);
    }
  }
  arr.push(1);
  return arr.sort((a, b) => b - a);
};
```

D:
```js
const getOddCollatz = (n) => {
  let arr = [];
  while (n !== 1) {
    if (n % 2 === 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
      arr.unshift(n);
    }
  }
  arr.push(1);
  return arr;
};
```

E:
```js
const getOddCollatz = (n) => {
  let arr = [];
  while (n !== 1) {
    if (n % 2 === 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
      arr.push(n);
    }
  }
  arr.push(1);
  return arr.slice().sort((a, b) => a - b);
};
```

F:
```js
const getOddCollatz = (n) => {
  let arr = [];
  while (n !== 1) {
    if (n % 2 === 0) {
      n = n /