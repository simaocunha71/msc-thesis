  if(n === 1){
    return x === 1;
  }
  if(n === 0){
    return x === 0;
  }
  let power = 1;
  while(power < x){
    power *= n;
    if(power === x){
      return true;
    }
  }
  return false;
}

console.log(isSimplePower(1, 4)) // true
console.log(isSimplePower(2, 2)) // true
console.log(isSimplePower(8, 2)) // true
console.log(isSimplePower(3, 2)) // false
console.log(isSimplePower(3, 1)) // false
console.log(isSimplePower(5, 3)) // false

```

The function works by keeping multiplying the variable "power" by "n" until "power" is equal or greater than "x". If at any point "power" equals "x", the function returns true, indicating that "x" is a simple power of "n". If the loop completes without "power" ever equaling "x", the function returns false, indicating that "x" is not a simple power of "n". The function also handles the special cases where "n" is 0 or 1, which are the base cases for simple powers.
```

## 7. Sum of Multiples

```javascript
