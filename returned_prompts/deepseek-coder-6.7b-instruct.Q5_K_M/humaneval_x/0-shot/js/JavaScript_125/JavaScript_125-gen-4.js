  if(txt.indexOf(' ') !== -1) {
    return txt.split(' ')
  } else if(txt.indexOf(',') !== -1) {
    return txt.split(',')
  } else {
    let count = 0;
    for(let i = 0; i < txt.length; i++) {
      if(txt.charAt(i) === txt.charAt(i).toLowerCase() && i % 2 !== 0) {
        count++;
      }
    }
    return count;
  }
};
console.log(splitWords("Hello world!"))
console.log(splitWords("Hello,world!"))
console.log(splitWords("abcdef"))
```

The program works by first checking if the input string contains a whitespace or a comma. If it does, it splits the string at that character and returns the resulting array of words. If the string doesn't contain either, it counts the number of lowercase letters with an odd index (since indexing starts at 0, the second letter has an index of 1, the fourth has an index of 3, etc.) and returns that count.

This solution assumes that the input string only contains letters and numbers, and that the count should not include any characters that are not lowercase or are not in the first half of the alphabet (since the question specifies that the order should be odd).

If this is not the case, the function will need to be adjusted accordingly.

Also, please note that the function does not account for uppercase letters or any other special characters. If this is a possibility, you will need to add additional checks to handle these cases.
*/

// Test cases:
console.log(splitWords("Hello world!")) // ➞ ["Hello", "world!"]
console.log(splitWords("Hello,world!")) // ➞ ["Hello", "world!"]
console.log(splitWords("abcdef")) // ➞ 3
console.log(splitWords("Test123")) // ➞ 2
console.log(splitWords("AbCdEf")) // ➞ 3
console.log(splitW