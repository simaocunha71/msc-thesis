const checkIfLastCharIsALetter = (txt) => {
  const lastChar = txt[txt.length - 1];
  const lastCharIndex = txt.lastIndexOf(' ');
  return (lastChar === ' ' || lastChar === '') && (lastChar.match(/[a-z]/i) !== null);
};


// test here
console.log(checkIfLastCharIsALetter("apple pie"));       // false
console.log(checkIfLastCharIsALetter("apple pi e"));     // true
console.log(checkIfLastCharIsALetter("apple pi e "));     // false
console.log(checkIfLastCharIsALetter(""));                // false
console.log(checkIfLastCharIsALetter("abc "));            // true

*/

// practice

const checkIfLastCharIsALetter = (txt) => {
  const lastChar = txt[txt.length - 1];
  const lastCharIndex = txt.lastIndexOf(' ');
  return (lastChar === ' ' || lastChar === '') && (lastChar.match(/[a-z]/i) !== null);
};

// test here
console.log(checkIfLastCharIsALetter("apple pie"));       // false
console.log(checkIfLastCharIsALetter("apple pi e"));     // true
console.log(checkIfLastCharIsALetter("apple pi e "));     // false
console.log(checkIfLastCharIsALetter(""));                // false
console.log(checkIfLastCharIsALetter("abc "));            // true



































































































































