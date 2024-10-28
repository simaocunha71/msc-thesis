  const hexPrime = ['2', '3', '5', '7', 'B', 'D'];
  let count = 0;
  for (let i = 0; i < num.length; i++) {
    if (hexPrime.includes(num[i])) {
      count++;
    }
  }
  return count;
};

console.log(hexKey("AB")); //1
console.log(hexKey("1077E")); //2
console.log(hexKey("ABED1A33")); //4
console.log(hexKey("123456789ABCDEF0")); //6
console.log(hexKey("2020")); //2

// Note: This function works by iterating over each character of the input string and checking if it is present in the array of hexadecimal prime numbers. If it is, the count is incremented.
// Finally, the function returns the count.

```

## JavaScript

```javascript
