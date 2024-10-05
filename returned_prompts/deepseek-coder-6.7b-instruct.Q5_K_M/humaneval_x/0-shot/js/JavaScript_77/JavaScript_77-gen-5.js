  let n = Math.round(Math.abs(a) ** (1/3));
  return n * n * n === Math.abs(a);
}

console.log(iscube(1)); //true
console.log(iscube(2)); //false
console.log(iscube(-1)); //true
console.log(iscube(64)); //true
console.log(iscube(0)); //true
console.log(iscube(180)); //false

// This function works by first taking the absolute value of the input and cubing it.
// Then it takes the cube root of the result, rounding to the nearest integer.
// It then checks if the cube of that rounded integer is equal to the original absolute value. 
// If it is, then the original value was a cube, so the function returns true. If not, then it returns false.
```

## 2.

```javascript
