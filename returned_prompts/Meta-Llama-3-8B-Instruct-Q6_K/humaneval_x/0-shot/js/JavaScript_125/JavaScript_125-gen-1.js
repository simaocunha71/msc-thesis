Here is the solution in JavaScript:
```
const splitWords = (txt) => {
  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt.charCodeAt(i) >= 'a'.charCodeAt(0) && txt.charCodeAt(i) <= 'z'.charCodeAt(0) && (txt.charCodeAt(i) - 'a'.charCodeAt(0)) % 2 !== 0) {
        count++;
      }
    }
    return count;
  }
};
```
Here's an explanation of the solution:

1. If the input string contains whitespace characters, we split it using the `split()` method with a space character as the separator.
2. If the input string contains commas, we split it using the `split()` method with a comma character as the separator.
3. If the input string does not contain whitespace or commas, we iterate through the characters of the string and check if each character is a lowercase letter (using the `charCodeAt()` method) and if it has an odd index in the alphabet (using the modulo operator). If it does, we increment a counter. Finally, we return the count.

You can test the function with the examples you provided:
```
console.log(splitWords("Hello world!")); // Output: ["Hello", "world!"]
console.log(splitWords("Hello,world!")); // Output: ["Hello", "world!"]
console.log(splitWords("abcdef")); // Output: 3
``` A: Here is the solution in JavaScript:
```
const splitWords = (txt) => {
  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt.charCodeAt(i) >= 'a'.charCodeAt(0) && txt.charCodeAt(i) <= 'z'.charCodeAt(0) && (txt.charCodeAt(i) - 'a'.charCodeAt(0)) % 2 !== 0) {
        count++;
      }
    }
    return count;
  }
};
```
Here's an explanation of the solution:

1. If the input string contains whitespace characters, we split it using