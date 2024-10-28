  return text.replace(/\s+/g, match => {
    if (match.length === 1) {
      return '_';
    } else {
      return '-';
    }
  });
};


console.log(fixSpaces("Example")); // "Example"
console.log(fixSpaces("Example 1")); // "Example_1"
console.log(fixSpaces(" Example 2")); // "_Example_2"
console.log(fixSpaces(" Example  3")); // "_Example-3"


The regular expression /\s+/g matches one or more whitespace characters. The callback function is invoked for every match. If the length of the match is 1, it means the match is a single space, and it's replaced with an underscore. If the length of the match is greater than 1, it means the match is a sequence of spaces, and it's replaced with a dash.

This solution assumes that the input string will not contain other special characters or numbers that could be mistaken for spaces.
*/




const fixSpaces = (text) => {
  return text.replace(/ {2,}/g, '_').replace(/ /g, '_');
};


console.log(fixSpaces("Example")); // "Example"
console.log(fixSpaces("Example 1")); // "Example_1"
console.log(fixSpaces(" Example 2")); // "_Example_2"
console.log(fixSpaces(" Example  3")); // "_Example_3"


The regular expression / {2,}/g matches two or more consecutive spaces. The replace() function is used to replace these matches with an underscore. The regular expression / /g matches any single space and is also used to replace these matches with an underscore.

This solution assumes that the input string will not contain other special characters or numbers that could be mistaken for spaces.


*/
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4: Given a string of numbers, write a function to return the number of occurrences of each digit in the string.
<jupyter_code>
/*
