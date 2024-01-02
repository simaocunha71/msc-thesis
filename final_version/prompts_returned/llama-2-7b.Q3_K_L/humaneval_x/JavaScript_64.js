/*Write a function vowelsCount which takes a string representing
  a word as input and returns the number of vowels in the string.
  Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
  vowel, but only when it is at the end of the given word.

  Example:
  >>> vowelsCount("abcde")
  2
  >>> vowelsCount("ACEDY")
  3
  */
const vowelsCount = (s) => {
  let i;
  const vowelCharacters = new Set();
  for (i = 0, s.length > i; i < s.length) {
    if(vowelCharacters.has(s[i])) {
      return i + 1;
    } else {
      vowelCharacters.add(s[i]);
    }
  }
};