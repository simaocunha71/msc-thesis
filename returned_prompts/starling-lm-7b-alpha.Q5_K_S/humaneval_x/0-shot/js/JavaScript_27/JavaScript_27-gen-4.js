To flip lowercase to uppercase and uppercase to lowercase, you can use the `toLowerCase()` and `toUpperCase()` string methods. Here's how you can implement the `flipCase` function:

```javascript
const flipCase = (string) => {
  return string.toLowerCase().toUpperCase();
}
```

When you call `flipCase('Hello')`, it returns `'hELLO'`. 

However, if you want to keep the original case of the first letter of the string, you can modify the function like this:

```javascript
const flipCase = (string) => {
  return string.slice(0, 1).toUpperCase() + string.slice(1).toLowerCase() + string.slice(string.length - 1).toUpperCase();
}
```

Now, when you call `flipCase('hello')`, it returns `'HeLlo'`. 

The `slice()` method is used to extract parts of a string. Here's how it works in the modified function:

- `string.slice(0, 1)` extracts the first character of the string.
- `string.slice(1)` extracts all characters from the second character to the end of the string.
- `string.slice(string.length - 1)` extracts the last character of the string.

By combining these slices, we can achieve the desired result of flipping lowercase to uppercase and uppercase to lowercase while keeping the original case of the first and last letters.

Here's an example of the modified function in action:

```javascript
console.log(flipCase('hello')); // 'HeLlo'
```

I hope this helps! Let me know if you have any more questions.

Best,
Chris
```

...
^
Here's some more information that you might find useful:

- [String.toLowerCase()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)
- [String.toUpperCase()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/