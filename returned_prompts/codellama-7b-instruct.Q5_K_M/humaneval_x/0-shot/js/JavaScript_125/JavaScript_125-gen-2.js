/* Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
  should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
  alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
  Examples
  splitWords("Hello world!") ➞ ["Hello", "world!"]
  splitWords("Hello,world!") ➞ ["Hello", "world!"]
  splitWords("abcdef") == 3
  */
const splitWords = (txt) => {
  const words = txt.trim().split(/\s+|,+/);
  if (words.length > 1) {
    return words;
  }
  let sum = 0;
  for (let i = 0; i < txt.length; i++) {
    if (txt[i].toLowerCase() === txt[i] && (i % 2 !== 0)) sum++;
  }
  return sum;
};
