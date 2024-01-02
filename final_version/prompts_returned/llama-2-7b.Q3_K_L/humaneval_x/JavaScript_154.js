/*You are given 2 words. You need to return true if the second word or any of its rotations is a substring in the first word
  cycpatternCheck("abcd","abd") => false
  cycpatternCheck("hello","ell") => true
  cycpatternCheck("whassup","psus") => false
  cycpatternCheck("abab","baa") => true
  cycpatternCheck("efef","eeff") => false
  cycpatternCheck("himenss","simen") => true
  */
const cycpatternCheck = (a, b) => {
  const letters = a.split('');
  let result;
  b.split('').forEach((letter, i) => {
    if ((letters[i] === letter) && (result || !result)) {
      result = true;
    } else {
      result = false;
    }
  });
  return result ? true : false;
};
console.log(cycpatternCheck('abcd','abd'));
