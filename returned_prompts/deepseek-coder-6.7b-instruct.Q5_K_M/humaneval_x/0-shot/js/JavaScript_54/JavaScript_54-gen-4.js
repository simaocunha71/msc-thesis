  const count = char => str =>
    [...str].reduce((acc, curr) => curr === char ? acc + 1 : acc, 0)

  const countChars = str => [...new Set([...str])].map(char => char)
    .reduce((acc, char) => ({...acc, [char]: count(char)(str)}), {})

  const s0Chars = countChars(s0)
  const s1Chars = countChars(s1)

  return Object.keys(s0Chars).every(key => s0Chars[key] === s1Chars[key])
}

console.log(sameChars('eabcdzzzz', 'dddzzzzzzzddeddabc')) // true
console.log(sameChars('abcd', 'dddddddabc')) // true
console.log(sameChars('dddddddabc', 'abcd')) // true
console.log(sameChars('eabcd', 'dddddddabc')) // false
console.log(sameChars('abcd', 'dddddddabce')) // false
console.log(sameChars('eabcdzzzz', 'dddzzzzzzzddddabc')) // false

*/
```

This function works by first creating a helper function `count` which counts the occurrences of a given character in a string. It then creates a second helper function `countChars` which creates an object with the character counts for each character in a string. The function `sameChars` then checks if the character counts for each character in the first string match the character counts for each character in the second string.

The function `sameChars` returns true if all characters in the first string appear the same number of times in the second string, and false otherwise.

This solution has a time complexity of O(n), where n is the length of the longest string, because it needs to iterate over each character in both strings once. It also has a space complexity of O(n), because it creates an object with a key for each unique character in the strings.

The function `sameChars` is case-sensitive, meaning it treats uppercase and lowercase characters