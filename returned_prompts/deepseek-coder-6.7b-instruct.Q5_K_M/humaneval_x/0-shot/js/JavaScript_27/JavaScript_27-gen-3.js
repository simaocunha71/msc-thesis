  return string.split('').map(char => {
    return char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
  }).join('');

};

console.log(flipCase('Hello')); // 'hELLO'

// split the string into an array of characters
// map over each character, checking if it's upper case or lower case
// if it's uppercase, make it lowercase, else make it uppercase
// join the array back together into a string
```

### Exercise 3:

```js
