  for(let i = y; i >= x; i--) {
    if(i % 2 === 0) {
      return i;
    }
  }
  return -1;
}

// Test cases
console.log(chooseNum(12, 15)); // 14
console.log(chooseNum(13, 12)); // -1
console.log(chooseNum(8, 10)); // 10
console.log(chooseNum(9, 11)); // -1

// The function checks from the end of the range to the start
// if the number is even, it returns that number. If not, it keeps going
// if there are no even numbers in the range, it returns -1.

// Test cases
console.log(chooseNum(12, 15)); // 14
console.log(chooseNum(13, 12)); // -1
console.log(chooseNum(8, 10)); // 10
console.log(chooseNum(9, 11)); // -1
```

# 6. 
```js
