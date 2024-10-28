  for(let i = y; i >= x; i--){
    if(i % 2 === 0){
      return i;
    }
  }
  return -1;
}

console.log(chooseNum(12,15)); // 14
console.log(chooseNum(13,12)); // -1
console.log(chooseNum(14,17)); // 16
console.log(chooseNum(15,19)); // 18
console.log(chooseNum(16,20)); // 20
console.log(chooseNum(17,21)); // 20
console.log(chooseNum(18,22)); // 20
console.log(chooseNum(19,23)); // 22
```

## 6. Create a function that returns the first prime number after a given integer.

