  let vowels = ["a", "e", "i", "o", "u", "y"];
  let count = 0;
  for(let i = 0; i < s.length; i++){
    if(vowels.includes(s[i].toLowerCase())){
      count++;
    }
  }
  return count;
}

console.log(vowelsCount("abcde"));
console.log(vowelsCount("ACEDY"));

```

The function `vowelsCount` starts by creating an array of vowels. It then initializes a counter variable `count` to 0.

Then it loops through each character in the input string, `s`. If the character is a vowel (including 'y' at the end of the word), it increments the count.

Finally, it returns the total count of vowels. The function also converts the input string to lowercase before checking to ensure that the function is case insensitive.
*/

// 2.
```js
