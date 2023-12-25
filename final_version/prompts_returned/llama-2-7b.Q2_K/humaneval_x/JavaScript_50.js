/*
  returns encoded string by shifting every character by 5 in the alphabet.
  */
const encodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) + 5 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
}

/*
  takes as input string encoded with encode_shift function. Returns decoded string.
  */
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode((ch - "a".charCodeAt(0)) + 26)).join("");
}

/*
returns true if input string consists of 3 or more chars and every char is a vowel (except for 'y')
*/
const isVowelsString = (s) => {
   const firstLetterNotY = s.split("").map(ch => String.fromCharCode((ch.charCodeAt(0) % 26 + "a".charCodeAt(0))).includes('y')? 'a': ch);
   return firstLetterNotY == 'a' && firstLetterNotY == 'e';
}
/*
returns true if input string consists of at least one letter not a vowel (except for 'y').
*/
const isConsonantsString = (s) => {
  const firstLetterNotVowel = s.split("").map(ch => String.fromCharCode((ch % 26 + "a".charCodeAt(0))).includes('y')? 'a': ch);
   return firstLetterNotVowel == 'a';
}
/*
returns true if input string consists of only letters (except for y) and does not consist solely of vowels.
*/
const isPureConsonant = (s) => {
  const consonantsString = s.split("").map(ch => String.fromCharCode((ch - "a".charCodeAt(0)) + "a".charCodeAt(0)).includes('y')? 'a': ch); // if input string is not vowels, return it
