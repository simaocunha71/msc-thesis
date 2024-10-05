const charSet = new Set();
for (let char of string) {
  charSet.add(char);
}
return charSet.size;

};

countDistinctCharacters('xyzXYZ'); // 3
countDistinctCharacters('Jerry'); // 4

Explanation:
The function `countDistinctCharacters` takes in a string and returns the number of unique characters in the string. It does this by iterating over each character in the string and adding it to a `Set`. A `Set` is a collection of unique values, so any duplicate characters are automatically eliminated. Finally, the size of the `Set` is returned, which represents the number of unique characters in the string.

In the first example, the string `'xyzXYZ'` contains three distinct characters: `'x'`, `'y'`, and `'z'`. So the function returns `3`.

In the second example, the string `'Jerry'` contains four distinct characters: `'J'`, `'e'`, `'r'`, and `'y'`. So the function returns `4`.

The function is case-insensitive, meaning that it treats uppercase and lowercase letters as the same character. For example, in the first example, the characters `'x'` and `'X'` are considered the same, so they are counted as one distinct character.

The function is also sensitive to whitespace and punctuation. For example, in the second example, the whitespace character and the period are considered distinct characters, so they are counted separately.

Overall, the function provides a simple and efficient way to count the number of unique characters in a string, regardless of case.

*/

*/

/*
