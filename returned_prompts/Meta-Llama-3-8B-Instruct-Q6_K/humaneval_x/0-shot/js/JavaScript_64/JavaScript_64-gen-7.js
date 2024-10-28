Here is a possible solution:
```
const vowelsCount = (s) => {
  const vowels = 'aeiou';
  let count = 0;
  for (let char of s.toLowerCase()) {
    if (vowels.includes(char)) {
      count++;
    }
  }
  return count;
};
```
Here's an explanation of the code:

* We define a constant `vowels` containing the vowels we're interested in.
* We initialize a variable `count` to 0, which will store the number of vowels found.
* We iterate over the characters of the input string `s` using a `for...of` loop. We convert each character to lowercase using the `toLowerCase()` method, so that we can ignore case when checking for vowels.
* Inside the loop, we check if the current character is included in the `vowels` string using the `includes()` method. If it is, we increment the `count` variable.
* Finally, we return the `count` variable, which now holds the number of vowels found in the input string.

Note that this implementation assumes that the input string only contains ASCII characters. If you need to support non-ASCII characters, you may need to modify the implementation accordingly.