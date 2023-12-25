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
  const regex = new RegExp('[aeiouy]', 'gi'); // "y" is a vowel only at the end of the string. Hence, only need to check the last character.
  return s.match(regex).length;
};
