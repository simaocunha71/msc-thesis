  const min = Math.min(...numbers)
  const max = Math.max(...numbers)
  const range = max - min

  return numbers.map(n => (n - min) / range)
}

console.log(rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])) // [0, 0.25, 0.5, 0.75, 1]

```

## Functional Programming and Array Methods

```javascript
