  l.sort((a, b) => a - b);
  let mid = Math.floor(l.length / 2);

  if(l.length % 2 === 0) {
    return (l[mid - 1] + l[mid]) / 2;
  } else {
    return l[mid];
  }
}
```

### 9. Fibonacci Sequence

