  let res = [];

  for(let i = 1; i < xs.length; i++){
    res.push(xs[i] * i);
  }

  return res;
}

console.log(derivative([3, 1, 2, 4, 5])); // [1, 4, 12, 20]
console.log(derivative([1, 2, 3])); // [2, 6]

```

## 4. Array Sum

