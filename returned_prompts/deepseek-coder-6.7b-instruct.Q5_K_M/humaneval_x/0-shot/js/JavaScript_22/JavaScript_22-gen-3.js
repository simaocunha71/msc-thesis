  return values.filter(value => Number.isInteger(value));
}

console.log(filterIntegers(['a', 3.14, 5])) // [5]
console.log(filterIntegers([1, 2, 3, 'abc', {}, []])) // [1, 2, 3]
```

