  let words = txt.split(/\s+/);
  if (words.length === 1 && txt.indexOf(',') === -1) {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt[i].toLowerCase() >= 'a' && txt[i].toLowerCase() <= 'z' && (i + 1) % 2 !== 0) {
        count++;
      }
    }
    return count;
  }
  return words;
}
// Test cases
console.log(splitWords("Hello world!")); // ➞ ["Hello", "world!"]
console.log(splitWords("Hello,world!")); // ➞ ["Hello", "world!"]
console.log(splitWords("abcdef")); // ➞ 3
console.log(splitWords("")); // ➞ []



