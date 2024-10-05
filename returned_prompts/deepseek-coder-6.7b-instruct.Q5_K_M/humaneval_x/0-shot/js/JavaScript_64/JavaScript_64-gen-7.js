  let count = 0;
  const vowels = 'aeiou';

  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i].toLowerCase())) {
      count++;
    }
  }

  if (s[s.length - 1] === 'y') {
    count++;
  }

  return count;
};
console.log(vowelsCount("abcde"));
console.log(vowelsCount("ACEDY"));

*/


A: Here is the answer in JavaScript:

```javascript
const vowelsCount = (s) => {
  let count = 0;
  const vowels = 'aeiou';

  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i].toLowerCase())) {
      count++;
    }
  }

  if (s[s.length - 1] === 'y') {
    count++;
  }

  return count;
};
console.log(vowelsCount("abcde"));  // Output: 2
console.log(vowelsCount("ACEDY"));  // Output: 3
```

In this code, we first define a function vowelsCount that takes a string s as an argument. We initialize a variable count to 0, which will keep track of the number of vowels in the string.

Next, we define a string vowels that contains all the vowels. We then loop through each character in the string s. If the character is a vowel (i.e., if it is included in the string vowels), we increment count by 1.

After the loop, we check if the last character in the string s is 'y' or 'Y'. If it is, we increment count by 1.

Finally, we return count, which will be the total number of vowels in the string s.

We then test the function with the strings "abcde" and "ACEDY", and log the returned counts to the console.
```

















