To determine if a string is a palindrome, we need to check if it reads the same backward as forward. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

Here's how you can implement the `isPalindrome` function in JavaScript:

```javascript
const isPalindrome = (text) => {
  // Remove any non-alphanumeric characters and convert to lowercase
  const cleanedText = text.replace(/[^a-z0-9]/gi, '').toLowerCase();
  
  // Check if the cleaned text is the same as its reverse
  return cleanedText === cleanedText.split('').reverse().join('');
};
```

This function works as follows:
1. It uses a regular expression (`/[^a-z0-9]/gi`) to find all non-alphanumeric characters in the text. The `g` flag indicates a global search, and the `i` flag makes the search case-insensitive. The `replace` method then replaces these characters with an empty string, effectively removing them.
2. The `toLowerCase` method is used to convert the cleaned text to lowercase, ensuring that the palindrome check is case-insensitive.
3. The function then checks if the cleaned text is the same as its reverse. This is done by:
   - Splitting the cleaned text into an array of characters using `split('')`.
   - Reversing the array using `reverse()`.
   - Joining the reversed array back into a string using `join('')`.
4. If the cleaned text and its reverse are the same, the function returns `true`, indicating that the original text is a palindrome. Otherwise, it returns `false`.

The provided examples demonstrate how the `isPalindrome` function can be used to check for palindromes in various strings.