```javascript
const isHappy = (s) => {
  if (s.length < 3) return false;
  for (let i = 0; i < s.length - 2; i++) {
    if (s[i] === s[i + 1] || s[i] === s[i + 2] || s[i + 1] === s[i + 2]) {
      return false;
    }
  }
  return true;
};
```
Explanation:
The function checks if the string `s` is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

The function first checks if the length of the string is less than 3. If it is, the function returns `false` because a string with a length less than 3 cannot be happy.

Then, the function loops through the string using a for loop. The loop starts from the first character of the string and goes up to the third last character of the string.

Inside the loop, the function checks if the current character is the same as the next character or the next character is the same as the character after next. If any of these conditions is true, the function returns `false` because it means that every 3 consecutive letters are not distinct.

If the loop finishes without returning `false`, the function returns `true` because it means that every 3 consecutive letters are distinct. This means that the string is happy.

The function uses a simple and efficient algorithm to solve the problem. It has a time complexity of O(n), where n is the length of the string, and a space complexity of O(1), which means it uses a constant amount of space. This makes the function suitable for large strings.