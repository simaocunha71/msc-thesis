The task is to create a function `flipCase` that takes a string as input and returns a new string where all lowercase characters are converted to uppercase and all uppercase characters are converted to lowercase.

Here is the solution:
```
const flipCase = (string) => {
  return string.split('').map((char) => {
    if (char === char.toUpperCase()) {
      return char.toLowerCase();
    } else {
      return char.toUpperCase();
    }
  }).join('');
};
```
This function works by first splitting the input string into an array of individual characters using `split('')`. Then, it uses the `map` method to iterate over each character in the array. For each character, it checks if the character is uppercase using `char === char.toUpperCase()`. If it is, it converts it to lowercase using `char.toLowerCase()`, and if it's not, it converts it to uppercase using `char.toUpperCase()`. Finally, it uses the `join('')` method to concatenate the modified characters back into a string. The resulting string is the flipped case of the original input string.