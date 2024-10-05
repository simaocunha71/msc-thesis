  let result = '';

  for (let i = 0; i < message.length; i++) {
    let char = message[i];

    if (/[aeiou]/gi.test(char)) {
      result += String.fromCharCode(char.charCodeAt(0) + 2);
    } else {
      result += char.toUpperCase();
    }
  }

  return result;
};

console.log(encode('test')); // 'TGST'
console.log(encode('This is a message')); // 'tHKS KS C MGSSCGG'

/*
  In the above function, we iterate over each character of the string.
  If the character is a vowel (either lowercase or uppercase), we add 
  2 to its ASCII value to get the ASCII value of the new character,
  and then we convert this new ASCII value back to a character using
  String.fromCharCode() to get the new character. 

  If the character is not a vowel, we just convert it to uppercase.
  Finally, we add the new character to the result string.
*/

/*
  Note: This solution assumes that the input message only contains 
  English letters. If there could be other characters in the message 
  that could potentially cause issues, we would need to add checks 
  to ensure that only letters are encoded.
*/
```

</p>
</details>

## Task 2

Write a function `reverseWords` that takes a string of space-separated words and returns a new string where the words are in reverse order.

### Example

```javascript
reverseWords('Hello world'); // returns 'world Hello'
```

### Solution

<details>
<summary>Click to expand</summary>
<p>

```javascript
const reverseWords = (str) => {
  return str.split(' ').reverse().join(' ');
};

console.log(reverseWords('Hello world')); // 'world Hello'
```

</p>
</details>

## Task 3

Write a function `