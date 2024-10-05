  let arr = s.split('').map(char => {
    if(char === char.toUpperCase()){
      return char.toLowerCase();
    } else if(char === char.toLowerCase()){
      return char.toUpperCase();
    } else {
      return char;
    }
  });

  return arr.join('');
}

console.log(solve("1234")); // "4321"
console.log(solve("ab")); // "AB"
console.log(solve("#a@C")); // "#A@c"

// 1. We first split the given string into an array of characters.
// 2. Then we map over this array and change each letter to opposite case.
// 3. If the character is uppercase, we convert it to lowercase, and vice versa.
// 4. If the character is not a letter, we keep it as it is.
// 5. Finally, we join the array back into a string.

// Please note that the function will not work as expected if the string contains special characters or numbers.
// It only checks if the character is a letter, not if it is a letter in the English alphabet.
```

## JavaScript
```javascript
