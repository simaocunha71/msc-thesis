  let words = string.split(' ');
  let maxLength = 0;

  for (let i = 0; i < words.length; i++) {
    if (words[i].length > maxLength) {
      maxLength = words[i].length;
    }
  }

  return maxLength;
}

console.log(findLongestWordLength("The quick brown fox jumps over the lazy dog")) // returns 6
console.log(findLongestWordLength("May the force be with you")) // returns 5

*/

// Test cases:
console.log(find