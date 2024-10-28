return string.split('').map((char) => {
        return char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
    }).join('');
}

console.log(flipCase('Hello')); // 'hELLO'


// Explanation:
// The function `flipCase` takes a string as its argument.
// The string is split into an array of characters, then the array is mapped over.
// If the character is uppercase, it is converted to lowercase. If the character is lowercase, it is converted to uppercase.
// The resulting array of characters is then joined back into a single string.
// The resulting string is then returned.

// Test cases:
console.log(flipCase('Hello')); // 'hELLO'
console.log(flipCase('hELLO')); // 'Hello'
console.log(flipCase('JavaScrIpT')); // 'jAVAsCRiPt'
console.log(flipCase('12345')); // '12345'
console.log(flipCase('')); // ''
```


#### 3. Write a function `calculateAverage` that takes an array of numbers, and returns their average.

```javascript
