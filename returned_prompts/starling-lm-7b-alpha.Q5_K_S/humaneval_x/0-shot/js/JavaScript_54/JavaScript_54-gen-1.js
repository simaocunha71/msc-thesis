  // convert the strings to arrays of characters
  const s0Arr = [...s0];
  const s1Arr = [...s1];

  // sort the arrays
  s0Arr.sort();
  s1Arr.sort();

  // check if they are equal
  return s0Arr.every((char, index) => char === s1Arr[index]);
};

/*
  Check if two strings have the same characters.
  >>> sameChars('eabcdzzzz', 'dddzzzzzhaddeddabc')
  true
  >>> sameChars('abcd', 'dddddddabc')
  true
  >>> sameChars('dddddddabc', 'abcd')
  true
  >>> sameChars('eabcd', 'dddddddabc')
  false
  >>> sameChars('abcd', 'dddddddabce')
  false
  >>> sameChars('eabcdzzzz', 'dddzzzzzhadddabc')
  false
  */
module.exports = sameChars;

*/

// convert the strings to arrays of characters
const s0Arr = [...s0];
const s1Arr = [...s1];

// sort the arrays
s0Arr.sort();
s1Arr.sort();

// check if they are equal
return s0Arr.every((char, index) => char === s1Arr[index]);





















































































































































































