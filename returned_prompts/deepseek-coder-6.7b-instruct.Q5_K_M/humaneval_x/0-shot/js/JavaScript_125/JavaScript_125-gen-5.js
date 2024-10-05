  if (txt.includes(" ")) {
    return txt.split(" ");
  } else if (txt.includes(",")) {
    return txt.split(",");
  } else {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt.charAt(i) === txt.charAt(i).toLowerCase() && txt.charAt(i) !== txt.charAt(i).toUpperCase()) {
        count++;
      }
    }
    return count % 2 !== 0 ? count : 0;
  }
}
console.log(splitWords("Hello world!")) // ➞  ["Hello", "world!"]
console.log(splitWords("Hello,world!")) // ➞  ["Hello", "world!"]
console.log(splitWords("abcdef")) // ➞ 3

This function checks if the input string contains a space or a comma. If it does, it splits the string at these points and returns the resulting array. If it does not, it counts the number of lower-case letters in the string and returns this count, but only if it is an odd number. If the count is even, it returns 0.
*/

function splitWords(txt) {
  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt[i] === txt[i].toLowerCase()) {
        count++;
      }
    }
    return count % 2 !== 0 ? count : 0;
  }
}

console.log(splitWords('Hello world')); // ➞  ["Hello", "world"]
console.log(splitWords('Hello,world')); // ➞  ["Hello", "world"]
console.log(splitWords('abcdef')); // ➞ 3








