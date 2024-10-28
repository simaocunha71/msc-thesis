```javascript
const flipCase = (string) => {
  return string.split('').map(c => c.toLowerCase() === c ? c.toUpperCase() : c.toLowerCase()).join('');
};
```
Explanation:

1. `split('')` splits the string into an array of individual characters.
2. `map()` applies a function to each character in the array. In this case, the function checks if the character is lowercase (using `c.toLowerCase() === c`) and if it is, it converts it to uppercase (using `c.toUpperCase()`). If the character is not lowercase, it leaves it as is.
3. `join('')` joins the modified characters back into a single string.

Test:
```javascript
console.log(flipCase('Hello')); // Output: 'hELLO'
``` 