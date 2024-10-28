```
const reverseDelete = (s, c) => {
  let result = '';
  for (let i = 0; i < s.length; i++) {
    let found = false;
    for (let j = 0; j < c.length; j++) {
      if (s[i] === c[j]) {
        found = true;
        break;
      }
    }
    if (!found) {
      result += s[i];
    }
  }
  return [result, isPalindrome(result)];
};

const isPalindrome = (s) => {
  let left = 0;
  let right = s.length - 1;
  while (left < right) {
    if (s[left] !== s[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
};
```
This solution iterates through the string `s` and checks if each character is present in the string `c`. If it is not, it adds the character to the result string. After all characters have been processed, it checks if the result string is a palindrome by comparing characters from the start and end of the string and moving towards the center. If the string is a palindrome, it returns a tuple containing the result string and `true`. Otherwise, it returns a tuple containing the result string and `false`. The `isPalindrome` function is a helper function that checks if a string is a palindrome. It does this by comparing characters from the start and end of the string and moving towards the center. If any pair of characters do not match, it returns `false`. If all pairs of characters match, it returns `true`.