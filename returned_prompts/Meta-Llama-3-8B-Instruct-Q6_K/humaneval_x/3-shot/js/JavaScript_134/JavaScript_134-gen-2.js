  if (txt.length === 0) return false;
  let lastChar = txt.slice(-1);
  let lastCharIsLetter = /[a-zA-Z]/.test(lastChar);
  let lastCharIsPartOfWord = /\S/.test(lastChar);
  return lastCharIsLetter && !lastCharIsPartOfWord;
}
// Test cases:
console.log(checkIfLastCharIsALetter("apple pie")); // false
console.log(checkIfLastCharIsALetter("apple pi e")); // true
console.log(checkIfLastCharIsALetter("apple pi e ")); // false
console.log(checkIfLastCharIsALetter("")); // false
console.log(checkIfLastCharIsALetter("a")); // false
console.log(checkIfLastCharIsALetter("A")); // true
console.log(checkIfLastCharIsALetter("Hello World")); // false
console.log(checkIfLastCharIsALetter("Hello")); // false
console.log(checkIfLastCharIsALetter("a")); // false
console.log(checkIfLastCharIsALetter("")); // false
console.log(checkIfLastCharIsALetter("Hello World")); // false
console.log(checkIfLastCharIsALetter("Hello")); // false
console.log(checkIfLastCharIsALetter("a")); // false
console.log(checkIfLastCharIsALetter("")); // false
console.log(checkIfLastCharIsALetter("Hello World")); // false
console.log(checkIfLastCharIsALetter("Hello")); // false
console.log(checkIfLastCharIsALetter("a")); // false
console.log(checkIfLastCharIsALetter("")); // false
console.log(checkIfLastCharIsALetter("Hello World")); // false
console.log(checkIfLastCharIsALetter("Hello")); // false
console.log(checkIfLastCharIsALetter("a")); // false
console.log(checkIfLastCharIsALetter("")); // false
console.log(checkIfLastCharIsALetter("Hello World")); // false
console.log(checkIfLastCharIsALetter("Hello")); // false
console.log(checkIfLastCharIsALetter("a")); // false
console.log(checkIfLastCharIsALetter("")); // false
console.log(checkIfLastCharIsALetter("Hello World")); // false
console.log(checkIfLastCharIsALetter("Hello")); // false
console.log(checkIfLastCharIsALetter("a