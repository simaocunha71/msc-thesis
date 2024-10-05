You can solve this problem by following these steps:

1. Initialize a variable `max` to store the maximum number of unique characters in any word and a variable `result` to store the word with maximum number of unique characters.
2. Iterate through each word in the given list of strings using a `for...of` loop.
3. For each word, create a new `Set` called `uniqueChars` to store all unique characters in the word. This can be done using the spread operator (`...`) to pass each character of the word as an argument to the `Set` constructor.
4. Check if the number of unique characters in the current word (`uniqueChars.size`) is greater than the current maximum (`max`). If so, update `max` and `result` to the current word.
5. If the number of unique characters in the current word is equal to the current maximum, compare the two words lexicographically using the `>` operator. If the current word is lexicographically smaller than `result`, update `result` to the current word.
6. After iterating through all the words, return the value of `result`.

By following these steps, you can find the word with the maximum number of unique characters or the word with the maximum number of unique characters that comes first in lexicographical order, depending on the requirements of the problem.

Here's an example implementation of the `findMax` function:

```javascript
function findMax(words) {
    let max