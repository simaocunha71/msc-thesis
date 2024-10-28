  const words = txt.split(' ');
  if(words.length === 1) {
    const wordsComma = txt.split(',');
    if(wordsComma.length === 1) {
      let count = 0;
      for(let i = 0; i < txt.length; i++) {
        if(txt[i] === txt[i].toLowerCase() && txt.charCodeAt(i) % 2 !== 0) {
          count++;
        }
      }
      return count;
    } else {
      return wordsComma;
    }
  } else {
    return words;
  }
}
console.log(splitWords("Hello world!")) // ➞  ["Hello", "world!"]
console.log(splitWords("Hello,world!")) // ➞  ["Hello", "world!"]
console.log(splitWords("abcdef")) // ➞  3

*/
The function splitWords takes a string txt as its input parameter. If the string contains a space, it splits the string into an array of words using the split() method. If the array's length is 1, it means that no spaces were found in the string. In such a case, it splits the string into an array of words using the comma as the delimiter. If the resulting array's length is still 1, it means that no commas were found in the string. In such a case, it counts the number of lower-case letters with an odd ASCII value (i.e., those that have an ASCII value such that the remainder when divided by 2 is not zero) and returns this count. Finally, it returns the array of words. Otherwise, it returns the array of words.



*/
/*

*/

































































































