  for(let i = y; i >= x; i--) {
    if(i % 2 === 0) {
      return i;
    }
  }
  return -1;
}

console.log(chooseNum(12, 15))  // 14
console.log(chooseNum(13, 12))  // -1
console.log(chooseNum(10, 20))  // 20
console.log(chooseNum(30, 50))  // 48
console.log(chooseNum(100, 150))  // 148
```

## 问题2
```javascript
