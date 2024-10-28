  return xs.slice(1).map((x, i) => x * (i + 1));
}

console.log(derivative([3, 1, 2, 4, 5])); // [1, 4, 12, 20]
console.log(derivative([1, 2, 3])); // [2, 6]

```

```javascript

