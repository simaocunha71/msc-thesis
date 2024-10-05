  return string.split('').map(char => {
    return char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
  }).join('');

}

console.log(flipCase('Hello')); // 'hELLO'

//Explanation:
//The function flipCase takes a string as an argument. The string is split into an array of characters.
//Then, using the map method, each character is converted to its opposite case.
//If the character is uppercase, it's converted to lowercase. If it's lowercase, it's converted to uppercase.
//The result is a new array of the same characters, but with flipped case.
//Finally, the join method is used to join these characters back into a single string.
//The flipped case string is returned.

//Test Cases:
console.log(flipCase('Hello')); // 'hELLO'
console.log(flipCase('JavaScript')); // 'jAVAsCRIPT'
console.log(flipCase('1234567890')); // '1234567890'
console.log(flipCase('Flip The Case')); // 'fLIP tHE cASE'
```

---

### Problem 4:

```js
