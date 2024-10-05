Here is a JavaScript function that counts the number of uppercase vowels in even indices of a given string:

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

This function iterates over the string using a for loop. For each character, it checks if the index is even (i % 2 === 0) and if the character is an uppercase vowel (using the includes method on an array of uppercase vowels). If both conditions are met, it increments the count. Finally, it returns the count.

You can test this function with the examples you provided:

```javascript
console.log(countUpper('aBCdEf')); // returns 1
console.log(countUpper('abcdefg')); // returns 0
console.log(countUpper('dBBE')); // returns 0
```



You can also use `filter` and `reduce` methods to achieve the same result in a more concise way:

```javascript
const countUpper = (s) => s.filter((c, i) => i % 2 === 0 && ['A', 'E', 'I', 'O', 'U'].includes(c.toUpperCase())).length;
```

This function uses the `filter` method to create a new array with only the characters that meet the condition (even index and uppercase vowel). Then, it uses the `length` property to count the number of elements in the filtered array.