/*You are given 2 words. You need to return true if the second word or any of its rotations is a substring in the first word
  cycpatternCheck("abcd","abd") => false
  cycpatternCheck("hello","ell") => true
  cycpatternCheck("whassup","psus") => false
  cycpatternCheck("abab","baa") => true
  cycpatternCheck("efef","eeff") => false
  cycpatternCheck("himenss","simen") => true
  */
const cycpatternCheck = (a, b) => {
  let flag = false;
  for (let i = 0; i < b.length; i++) {
    for (let j = i; j < b.length; j++) {
      if (a.indexOf(b.slice(i, j + 1)) !== -1) {
        flag = true;
        break;
      }
    }
    if