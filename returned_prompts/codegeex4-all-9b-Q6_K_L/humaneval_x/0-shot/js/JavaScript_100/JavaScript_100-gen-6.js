```
  const arr = Array.from({length: n}, (_, i) => i + 1);
  let i = 0;
  while (i < n) {
    if (arr[i] % 2 === 0) {
      arr[i] += 1;
    } else {
      arr[i] += 2;
    }
    i += 1;
  }
  return arr;
}
```