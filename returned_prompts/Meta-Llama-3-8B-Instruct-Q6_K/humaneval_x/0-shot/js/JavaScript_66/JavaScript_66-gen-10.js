Here is a JavaScript solution for the problem:
```
const digitSum = (s) => {
  let sum = 0;
  for (let char of s) {
    if (char.toUpperCase() === char) {
      sum += char.charCodeAt(0);
    }
  }
  return sum;
};
```
Explanation:

* We initialize a variable `sum` to 0, which will store the sum of the ASCII codes of the upper characters.
* We iterate over each character `char` in the input string `s` using a `for...of` loop.
* For each character, we check if it is an upper case character by comparing it with its upper case equivalent using the `toUpperCase()` method.
* If the character is an upper case character, we add its ASCII code to the `sum` variable using the `charCodeAt(0)` method.
* Finally, we return the `sum` variable, which contains the sum of the ASCII codes of the upper characters only.

This solution has a time complexity of O(n), where n is the length of the input string, because we iterate over each character in the string once. It also has a space complexity of O(1), because we only use a constant amount of space to store the `sum` variable.