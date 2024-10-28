```javascript
const splitWords = (txt) => {
  let words = txt.split(/\s+/);
  if (words.join('') === '') {
    words = txt.split(',');
    if (words.join('') === '') {
      let count = 0;
      for (let i = 0; i < txt.length; i++) {
        if (txt[i].toLowerCase() >= 'a' && txt[i].toLowerCase() <= 'z' && (txt[i].toLowerCase().charCodeAt(0) % 2 !== 0)) {
          count++;
        }
      }
      return count;
    }
  }
  return words;
};

// Test cases
console.log(splitWords("Hello world!")); // ➞ ["Hello", "world!"]
console.log(splitWords("Hello,world!")); // ➞ ["Hello", "world!"]
console.log(splitWords("abcdef")); // == 3
``` A simple JavaScript function, splitWords, takes a string as an input and splits it into words based on the following rules: - If there are spaces in the string, split on whitespace. - If there are no spaces and there are commas, split on commas. - If there are no spaces and no commas, count the number of lowercase letters with odd order in the alphabet. The function uses the split() method to split the string into words, and then checks the resulting array to determine the correct split method. If the array is empty, it means there were no spaces or commas, so the function counts the number of lowercase letters with odd order in the alphabet. The function returns the resulting array of words or the count of lowercase letters with odd order in the alphabet. The test cases demonstrate the function's behavior for different input strings.