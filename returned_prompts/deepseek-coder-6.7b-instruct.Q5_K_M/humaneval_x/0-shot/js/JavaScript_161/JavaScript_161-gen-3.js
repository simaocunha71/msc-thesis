  let arr = s.split('');
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].match(/[a-z]/i)) {
      arr[i] = arr[i] === arr[i].toUpperCase() ? arr[i].toLowerCase() : arr[i].toUpperCase();
    }
  }
  return arr.join('');
}

console.log(solve("1234")); // "4321"
console.log(solve("ab")); // "AB"
console.log(solve("#a@C")); // "#A@c"

/*
Explanation:
The solve function is taking a string s as argument.
It is splitting the string into an array of characters using the split method.
Then, a loop is running through the array.
If the character at the index i is a letter (checked by using a regular expression),
it is checking whether it is uppercase or lowercase.
If it is uppercase, it converts it to lowercase and vice versa.
Finally, all the characters in the array are joined back together into a string using the join method and returned.
*/

```

## JavaScript Code

```javascript
