return s.split(/[\s,]+/)

}

// TEST CASES
console.log(wordsString("Hi, my name is John")) //==  ["Hi", "my", "name", "is", "John"]
console.log(wordsString("One, two, three, four, five, six")) //==  ["One", "two", "three", "four", "five", "six"]


A: You can use the JavaScript String.prototype.split() method with a regex pattern that matches a comma or a space. 


const wordsString = (s) => {
    return s.split(/[\s,]+/);
}

console.log(wordsString("Hi, my name is John")); //["Hi", "my", "name", "is", "John"]
console.log(wordsString("One, two, three, four, five, six")); //["One", "two", "three", "four", "five", "six"]


In the regex pattern /[\s,]+/, \s matches any whitespace character, and , matches a literal comma. The + means one or more of the preceding element. So, this pattern will match one or more whitespace characters or commas.

A: Here is a simple solution using JavaScript's built-in String.prototype.split() method. This method splits a String object into an array of strings by separating the string into substrings, using a specified separator string to determine where to make each split.

```javascript
const wordsString = (s) => {
    return s.split(/[\s,]+/);
}

console.log(wordsString("Hi, my name is John")); //["Hi", "my", "name", "is", "John"]
console.log(wordsString("One, two, three, four, five, six")); //["One", "two", "three", "four", "five", "six"]
```

In the regular expression /[\s,]+/, \s matches any whitespace character, and , matches a literal comma. The + means one or more of the preceding element. So, this regex will match one or more whitespace characters or commas. This effectively separates the string into an array of words.

