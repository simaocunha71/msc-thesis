```
const isPalindrome = (text) => {
  if (!text) return true; // empty string is a palindrome
  const cleanText = text.replace(/[^a-zA-Z0-9]/g, '').toLowerCase(); // remove non-alphanumeric chars and convert to lowercase
  return cleanText === cleanText.split('').reverse().join(''); // compare with reversed string
};
```
Explanation:
1. Check if the input string is empty. If it is, return `true` since an empty string is a palindrome.
2. Remove non-alphanumeric characters from the string using a regular expression and convert the string to lowercase to ensure the comparison is case-insensitive.
3. Split the cleaned string into an array of individual characters, reverse the array, and join it back into a string.
4. Compare the original cleaned string with the reversed string. If they are the same, the string is a palindrome, and the function returns `true`. Otherwise, it returns `false`.