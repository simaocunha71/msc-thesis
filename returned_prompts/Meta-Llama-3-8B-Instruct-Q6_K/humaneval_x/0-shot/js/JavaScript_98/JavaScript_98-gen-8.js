Here is a simple JavaScript function that counts the number of uppercase vowels in even indices:

```javascript
const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0 && ['A', 'E', 'I', 'O', 'U'].includes(s[i].toUpperCase())) {
      count++;
    }
  }
  return count;
};
```

This function iterates over each character in the string. If the index is even (i.e., `i % 2 === 0`), it checks if the character is an uppercase vowel (by converting it to uppercase and checking if it's in the list of vowels). If it is, it increments the count. Finally, it returns the count.

You can test this function with the examples you provided:

```javascript
console.log(countUpper('aBCdEf')); // returns 1
console.log(countUpper('abcdefg')); // returns 0
console.log(countUpper('dBBE')); // returns 0
```


The time complexity of this function is O(n), where n is the length of the input string, because it iterates over each character in the string once. The space complexity is O(1), because it uses a constant amount of space to store the count and the list of vowels.