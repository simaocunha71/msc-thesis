/*
  Check if two words have the same characters.
  >>> sameChars('eabcdzzzz', 'dddzzzzzzzddeddabc')
  true
  >>> sameChars('abcd', 'dddddddabc')
  true
  >>> sameChars('dddddddabc', 'abcd')
  true
  >>> sameChars('eabcd', 'dddddddabc')
  false
  >>> sameChars('abcd', 'dddddddabce')
  false
  >>> sameChars('eabcdzzzz', 'dddzzzzzzzddddabc')
  false
  */
const sameChars = (s0, s1) => {
  const arr0 = s0.split('').sort();
  const arr1 = s1.split('').sort();
  return arr0.length === arr1.length && arr0.every((char, index) => char === arr1[index]);
}
