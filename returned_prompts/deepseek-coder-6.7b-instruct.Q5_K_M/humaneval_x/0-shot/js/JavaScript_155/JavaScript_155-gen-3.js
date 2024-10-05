  let str = Math.abs(num).toString();
  let even = 0;
  let odd = 0;
  
  for(let i = 0; i < str.length; i++) {
    if(str[i] % 2 === 0) {
      even++;
    } else {
      odd++;
    }
  }
  
  return [even, odd];
}

console.log(evenOddCount(-12)); // [1, 1]
console.log(evenOddCount(123)); // [1, 2]
console.log(evenOddCount(13579)); // [0, 5]
console.log(evenOddCount(2468)); // [4, 0]
console.log(evenOddCount(7777)); // [0, 4]
console.log(evenOddCount(1111)); // [0, 4]
```

## Task 4

```js
