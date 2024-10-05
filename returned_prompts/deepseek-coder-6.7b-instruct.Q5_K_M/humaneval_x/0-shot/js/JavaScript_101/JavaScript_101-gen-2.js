return s.split(/[ ,]+/);

};

console.log(wordsString("Hi, my name is John")); // ["Hi", "my", "name", "is", "John"]
console.log(wordsString("One, two, three, four, five, six")); // ["One", "two", "three", "four", "five", "six"]
console.log(wordsString("This is a test")); // ["This", "is", "a", "test"]
console.log(wordsString("Single word")); // ["Single word"]
console.log(wordsString("")); // [""]


/*
  The function wordsString uses the String.prototype.split method to split the string 
  at each occurrence of a comma or space, and return an array of the words. 
  The regular expression /[ ,]+/ is used as the separator, which matches one or more of any 
  type of space or comma.
  */

```

## --tests--

```javascript
const wordsString = require('./script');

describe("Testing wordsString function", () => {
    test("wordsString('Hi, my name is John') should return ['Hi', 'my', 'name', 'is', 'John']", () => {
        expect(wordsString('Hi, my name is John')).toEqual(['Hi', 'my', 'name', 'is', 'John']);
    });

    test("wordsString('One, two, three, four, five, six') should return ['One', 'two', 'three', 'four', 'five', 'six']", () => {
        expect(wordsString('One, two, three, four, five, six')).toEqual(['One', 'two', 'three', 'four', 'five', 'six']);
    });

    test("wordsString('This is a test') should return ['This', 'is', 'a', 'test']", () => {
        expect(wordsString('This is a test')).toEqual(['This', 'is', 'a', 'test']);
    });

    test("wordsString('Single word') should return ['Single', 'word']", () => {
        expect(wordsString('Single word')).toEqual(['