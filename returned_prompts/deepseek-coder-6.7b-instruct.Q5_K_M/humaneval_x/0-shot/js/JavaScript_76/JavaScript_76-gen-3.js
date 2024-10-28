  if(n === 1) return x > 0;
  while(x > 1){
    x /= n;
    if(x !== Math.floor(x)) return false;
  }
  return x === 1;
}

console.log(isSimplePower(1, 4)) //=> true
console.log(isSimplePower(2, 2)) //=> true
console.log(isSimplePower(8, 2)) //=> true
console.log(isSimplePower(3, 2)) //=> false
console.log(isSimplePower(3, 1)) //=> false
console.log(isSimplePower(5, 3)) //=> false

```

---

## 3. Find the area of a triangle

```javascript
