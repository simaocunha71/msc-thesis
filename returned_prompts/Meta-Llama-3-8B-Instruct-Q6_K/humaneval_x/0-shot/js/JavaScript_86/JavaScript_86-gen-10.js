Here is the solution using JavaScript:
```
const antiShuffle = (s) => {
  return s.split(' ').map(word => {
    return word.split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
  }).join(' ');
};
```
Explanation:

1. `s.split(' ')` splits the input string into an array of words, separated by spaces.
2. `map()` applies a transformation to each word in the array.
3. `word.split('')` splits each word into an array of individual characters.
4. `sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0))` sorts the characters in each word in ascending order based on their ASCII values.
5. `join('')` concatenates the sorted characters back into a string.
6. `join(' ')` concatenates the transformed words back into a single string, with spaces in between.

Example usage:
```
console.log(antiShuffle('Hi')); // Output: 'Hi'
console.log(antiShuffle('hello')); // Output: 'ehllo'
console.log(antiShuffle('Hello World!!!')); // Output: 'Hello !!!Wdlor'
```
This solution works by iterating over the input string, splitting it into words, sorting the characters in each word, and then concatenating the sorted words back into a single string. The order of words and blank spaces in the original sentence is preserved.