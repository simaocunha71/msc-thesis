  let sum = 0, product = 1;
  for(let i = 0; i < numbers.length; i++){
    sum += numbers[i];
    product *= numbers[i];
  }
  return (sum, product);
}

console.log(sumProduct([])); // (0, 1)
console.log(sumProduct([1, 2, 3, 4])); // (10, 24)
```

## 2. Write a function named "reverseCase" that will take a string as an argument and return a new string with all the letters of the original string in reverse case.

```javascript
