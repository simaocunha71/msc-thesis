  const histogram = (str) => str.split('').reduce((acc, char) => {
    acc[char] = (acc[char] || 0) + 1
    return acc
  }, {})

  const s0Hist = histogram(s0)
  const s1Hist = histogram(s1)

  if (Object.keys(s0Hist).length !== Object.keys(s1Hist).length) {
    return false
  }

  for (let char in s0Hist) {
    if (s0Hist[char] !== s1Hist[char]) {
      return false
    }
  }

  return true
}

// Test cases
console.log(sameChars('eabcdzzzz', 'dddzzzzzzzddeddabc')) // true
console.log(sameChars('abcd', 'dddddddabc')) // true
console.log(sameChars('dddddddabc', 'abcd')) // true
console.log(sameChars('eabcd', 'dddddddabc')) // false
console.log(sameChars('abcd', 'dddddddabce')) // false
console.log(sameChars('eabcdzzzz', 'dddzzzzzzzddddabc')) // false

```

This solution works by first creating a histogram of the characters in each string. The histogram is a map where the keys are the characters in the string and the values are the counts of those characters. If the histograms of the two strings are the same, then the strings have the same characters.

The time complexity of this solution is O(n) where n is the length of the string. This is because we are iterating over each character in both strings once. The space complexity is also O(n) because we are storing the histograms of the strings.

Note: This solution assumes that the input strings are case-sensitive, meaning 'a' and 'A' are considered different characters. If you want to ignore case, you can add a step to convert both strings to lower or upper case before creating the histograms.
*/

// Solution 2

const sameChars = (str1, str2