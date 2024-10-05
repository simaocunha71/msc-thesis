let flipped = '';
  
for (let i = 0; i < string.length; i++) {
  let char = string[i];
  
  if (char === char.toUpperCase()) {
    flipped += char.toLowerCase();
  } else {
    flipped += char.toUpperCase();
  }
}

return flipped;
}

console.log(flipCase('Hello'));

//Output: hELLO
```

**Output:**
```
hELLO
```

The function flipCase takes a string as an argument and iterates over each character in the string. It uses a ternary operator to check whether the character is uppercase or lowercase. If it is uppercase, it converts it to lowercase using the toLowerCase() method. If it is lowercase, it converts it to uppercase using the toUpperCase() method. This process is repeated until all characters in the string have been flipped.

The function then returns the flipped string.

## Task 2:

```js
// Write a function named "getDivisors" that takes a number as an argument and returns an array containing all the divisors of that number.

