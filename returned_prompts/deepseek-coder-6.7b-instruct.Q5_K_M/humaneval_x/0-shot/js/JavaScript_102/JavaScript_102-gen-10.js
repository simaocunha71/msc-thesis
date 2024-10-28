  for (let i = y; i >= x; i--) {
    if (i % 2 === 0) {
      return i;
    }
  }
  return -1;
}

console.log(chooseNum(12, 15)); // 14
console.log(chooseNum(13, 12)); // -1
console.log(chooseNum(14, 17)); // 16
console.log(chooseNum(15, 18)); // 18
console.log(chooseNum(16, 20)); // 18
```

### 3.
```js
