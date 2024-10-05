```javascript
const isHappy = (s) => {
  if (s.length < 3) {
    return false;
  }
  for (let i = 0; i <= s.length - 3; i++) {
    const window = s.slice(i, i + 3);
    if (new Set(window).size !== 3) {
      return false;
    }
  }
  return true;
};
```


Explanation:

1. First, we check if the length of the string is less than 3. If it is, we immediately return `false`, as a string with a length less than 3 cannot be happy.
2. We then use a for loop to create a sliding window of size 3 for each substring of the string.
3. For each window, we create a Set to store the unique characters in the window.
4. If the size of the Set is not equal to 3, it means that not all characters in the window are distinct, and we return `false`.
5. If the function has not returned `false` after checking all windows, it means that every 3 consecutive letters in the string are distinct, and we return `true`.

This solution has a time complexity of O(n), where n is the length of the input string, as we are iterating over the string once and performing a constant amount of work for each character. The space complexity is O(1), as we are using a fixed amount of space to store the Set and the variables used in the loop.