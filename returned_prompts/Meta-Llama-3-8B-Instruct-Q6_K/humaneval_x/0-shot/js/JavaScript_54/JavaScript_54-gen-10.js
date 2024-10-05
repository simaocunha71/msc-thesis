Here is the solution using JavaScript:
```
const sameChars = (s0, s1) => {
  const charCount0 = {};
  const charCount1 = {};

  for (let char of s0) {
    charCount0[char] = (charCount0[char] || 0) + 1;
  }

  for (let char of s1) {
    charCount1[char] = (charCount1[char] || 0) + 1;
  }

  return JSON.stringify(charCount0) === JSON.stringify(charCount1);
};
```
This function works by creating two objects, `charCount0` and `charCount1`, to count the frequency of each character in the two strings. It then compares the JSON representation of these two objects using `JSON.stringify`. If the two objects are equal, it means that the two strings have the same characters, and the function returns `true`. Otherwise, it returns `false`.