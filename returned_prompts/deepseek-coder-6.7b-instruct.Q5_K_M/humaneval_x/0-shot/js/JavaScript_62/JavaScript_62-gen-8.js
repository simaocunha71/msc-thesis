  let derivativeArray = [];
  for (let i = 1; i < xs.length; i++) {
    derivativeArray.push(xs[i] * i);
  }
  return derivativeArray;
};

console.log(derivative([3, 1, 2, 4, 5])); // [1, 4, 12, 20]
console.log(derivative([1, 2, 3])); // [2, 6]
```

## Question 3:

```javascript
