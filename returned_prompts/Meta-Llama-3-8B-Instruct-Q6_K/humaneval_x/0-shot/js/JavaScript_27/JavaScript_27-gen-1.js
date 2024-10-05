Here is the solution:

```javascript
const flipCase = (string) => {
  return string.split('').map((char) => {
    return char.charCodeAt(0) >= 97 ? String.fromCharCode(char.charCodeAt(0) - 32) : String.fromCharCode(char.charCodeAt(0) + 32);
  }).join('');
};
```

Explanation:

The function `flipCase` takes a string as an argument. It splits the string into an array of characters using the `split`` method. Then, it uses the `map` method to iterate over the array of characters. For each character, it checks if the character code is greater than or equal to 97 (which is the ASCII value of 'a'). If it is, it converts the character to uppercase by subtracting 32 from the character code using the `String.fromCharCode` method. If it's not, it converts the character to lowercase by adding 32 to the character code. Finally, it joins the array of characters back into a string using the `join`` method. The resulting string is the input string with all lowercase characters flipped to uppercase and all uppercase characters flipped to lowercase.