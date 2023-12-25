/*You are given 2 words. You need to return true if the second word or any of its rotations is a substring in the first word
  cycpatternCheck("abcd","abd") => false
  cycpatternCheck("hello","ell") => true
  cycpatternCheck("whassup","psus") => false
  cycpatternCheck("abab","baa") => true
  cycpatternCheck("efef","eeff") => false
  cycpatternCheck("himenss","simen") => true
  */
const cycpatternCheck = (a, b) => {
  const map = new Map();
  a.split('').map((element, index) => {
    if (!Array.isArray(element)) return; // don't pass strings to the following functions
    element[0] === 'e' ? element = element.toLowerCase() : null; // if the first character of each array is a-z or A-Z, convert it to lowercase
    const result = checkSubString(a, b, index);
    map.set('result', result);
  });
  return [...map.entries()][0][1]);
}
const checkSubString = (a, b, idx) => {
  if (idx === a.length - 1 && a[idx] !== 'e') return false; // if the last character is not equal to e it's not a substring of abcd
  const currentLetter = a.charAt(idx);
  let cIndex = b.indexOf(`${currentLetter}`);
  let rotations = [b];

  while (b && b !== 'e') {
    // console.log("Rotations", b)
    for (const rotation of b) { // rotate the substring by one position at a time, so if we start at 10 and it's substring is abcd -> [ 'a', 'd'], then when we want to check if it's substring of ['ab','c'] we need to rotate back to ['a','b']
    rotations.push(rotation); // now the array contains [ 'a','b','c','d']
    b = rotations[0]; // now we move onto the next rotation and check if