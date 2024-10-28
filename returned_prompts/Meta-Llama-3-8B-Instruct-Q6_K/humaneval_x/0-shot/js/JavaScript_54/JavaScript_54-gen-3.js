Here is the solution:
```
const sameChars = (s0, s1) => {
  if (s0.length !== s1.length) return false;
  const charCounts = {};
  for (let char of s0) {
    charCounts[char] = (charCounts[char] || 0) + 1;
  }
  for (let char of s1) {
    if (!charCounts[char] || charCounts[char] === 0) return false;
    charCounts[char]--;
  }
  return true;
};
```
Here's an explanation of the solution:

1. First, we check if the lengths of the two strings are the same. If they're not, we can immediately return `false`.
2. We create an object `charCounts` to keep track of the count of each character in the first string `s0`.
3. We iterate over each character in `s0` and increment its count in `charCounts`.
4. We then iterate over each character in the second string `s1`. For each character, we check if it's present in `charCounts` and if its count is greater than 0. If it's not present or its count is 0, we return `false`.
5. If we reach the end of the iteration without returning `false`, we return `true`, indicating that the two strings have the same characters.

This solution has a time complexity of O(n), where n is the length of the strings, because we iterate over each character in both strings once. The space complexity is O(1) because we use a fixed-size object to keep track of the character counts.