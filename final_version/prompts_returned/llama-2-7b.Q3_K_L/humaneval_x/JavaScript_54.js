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
  if (s0.length !== s1.length) return false;
  for (let i=0;i<s0.length;++i){
    if (s0[i]!==s1[i]) return false;
  }
  return true;
}
const main = () => {
  sameChars('eabcdzzzz', 'dddzzzzzzzddeddabc')
  sameChars('abcd', 'dddddddabc')
  sameChars('dddddddabc', 'abcd')
  sameChars('eabcd', 'dddddddabc')
  sameChars('abcd', 'dddddddabce')
  sameChars('eabcdzzzz', 'dddzzzzzzzddddabc')
}
main();