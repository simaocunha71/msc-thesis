  let increasing = true;
  let decreasing = true;

  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] > l[i + 1]) {
      increasing = false;
    }
    if (l[i] < l[i + 1]) {
      decreasing = false;
    }
  }

  return increasing || decreasing;
}

console.log(monotonic([1, 2, 4, 20])) // true
console.log(monotonic([1, 20, 4, 10])) // false
console.log(monotonic([4, 1, 0, -10])) // true

```

### Solution

```javascript

