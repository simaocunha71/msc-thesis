  const words = txt.split(' ');
  if (words.length === 1) {
    const chars = words[0].split(',');
    if (chars.length === 1) {
      let count = 0;
      for (let i = 0; i < chars[0].length; i++) {
        if (chars[0][i] === chars[0][i].toLowerCase() && chars[0][i] !== chars[0][i].toUpperCase() && (chars[0][i].charCodeAt(0) - 'a'.charCodeAt(0)) % 2 !== 0) {
          count++;
        }
      }
      return count;
    } else {
      return chars;
    }
  } else {
    return words;
  }
};

console.log(splitWords("Hello world!")) // ["Hello", "world!"]
console.log(splitWords("Hello,world!")) // ["Hello", "world!"]
console.log(splitWords("abcdef")) // 3

This function works by first checking if there are any spaces in the text. If not, it will split on commas. If there are no commas either, it will count the number of lower-case letters with odd order in the alphabet.
*/





































































































































































































