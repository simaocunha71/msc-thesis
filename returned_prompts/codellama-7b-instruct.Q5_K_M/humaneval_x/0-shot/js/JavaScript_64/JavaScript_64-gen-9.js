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
  let count = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === 'a' || s[i] === 'e' || s[i] === 'i' || s[i] === 'o' || s[i] === 'u' || (s[i] === 'y' && i === s.length - 1)) {
      count++;
    }
  }

  return count;
};

module.exports = vowelsCount;