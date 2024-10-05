To solve this problem, you can follow these steps:

1. Define a function called "isConsonant" that takes a character as input and returns true if the character is a consonant, and false otherwise. You can use a regular expression or a list of consonants to determine if a character is a consonant. Here's an example implementation:

```javascript
function isConsonant(c) {
    return c.match(/[^aeiou]/);
}
```

2. Define a function called "countConsonants" that takes a string as input and returns the count of consonants in the string. You can iterate through each character in the string and count the consonants using the "isConsonant" function. Here's an example implementation:

```javascript
function countConsonants(s) {
    return s.split("").reduce((total, c) => total + (isConsonant(c) ? 1 : 0), 0);
}
```

3. Define a function called "selectWords" that takes a string and a number as input and returns an array of words from the string that contain exactly n consonants. You can split the string into an array of words, filter the array based on the count of consonants using the "countConsonants" function, and return the filtered array. Here's an example implementation:

```javascript
function selectWords(s, n) {
    const words = s.split(" ");
    return words.filter(word => countConsonants(word) === n);
}
```

4. Test the "selectWords" function with different inputs to verify its correctness. Here are some example test cases:

```javascript
console.log(selectWords("Mary had a little lamb", 4)); // ["little"]
console.log(selectWords("Mary had a little lamb", 3)); // ["Mary")
console.log(selectWords("simple white space", 2)); // []
console.log(selectWords("Hello world", 4)); // ["world"]
console.log(selectWords("Uncle sam", 3)); // ["Uncle"]
```

