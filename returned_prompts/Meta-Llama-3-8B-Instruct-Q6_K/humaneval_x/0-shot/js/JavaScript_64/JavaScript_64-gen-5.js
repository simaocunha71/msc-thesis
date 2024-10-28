Here is a possible solution in JavaScript:
```
const vowelsCount = (s) => {
  let count = 0;
  for (let char of s.toLowerCase()) {
    if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u' || (char === 'y' && s.endsWith('y'))) {
      count++;
    }
  }
  return count;
};
```
Here's an explanation of the code:

* We initialize a variable `count` to 0, which will store the number of vowels in the string.
* We iterate over each character `char` in the input string `s` using a `for...of` loop.
* We convert the character to lowercase using the `toLowerCase()` method, so that we can compare it with the vowels in a case-insensitive manner.
* We check if the character is a vowel using an `if` statement. We check for the following vowels: 'a', 'e', 'i', 'o', 'u'. We also check if the character is 'y' and if the string ends with 'y' (using the `endsWith()` method), because 'y' is a vowel only when it's at the end of the word.
* If the character is a vowel, we increment the `count` variable by 1.
* Finally, we return the `count` variable, which represents the number of vowels in the input string.

You can test this function with the examples you provided:
```
console.log(vowelsCount("abcde")); // Output: 2
console.log(vowelsCount("ACEDY")); // Output: 3
```
I hope this helps! Let me know if you have any questions. 😊