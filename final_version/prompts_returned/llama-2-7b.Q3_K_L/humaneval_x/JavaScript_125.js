/* Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
  should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
  alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
  Examples
  splitWords("Hello world!") ➞ ["Hello", "world!"]
  splitWords("Hello,world!") ➞ ["Hello", "world!"]
  splitWords("abcdef") == 3
  */
const splitWords = (txt) => {
  const map = {};
  for (let i = 0; i < txt.length; i += 1) {
    if (!map[txt[i]]) {
      if (txt[i] === ",") {
        return [...map[","]];
      } else {
        map[txt[i]] = [];
      }
    }
    map[txt[i]].push(txt.slice(0, i));
  }
}
