/*Write a function vowelsCount which takes a string representing
  a word as input and returns the number of vowels in the string.
  Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
  vowels, but only when it is at the end of the given word.

  Example:
  >>> vowelsCount("abcde")
  2
  >>> vowelsCount("ACEDY")
  3
  */
  const vowelsCount = (s) => {
    let vowels = ['a', 'e', 'i', 'o', 'u', 'y'];
    let count = 0;
    for (let i = 0; i < s.length; i++) {
      if (vowels.indexOf(s[i]) !== -1) {
        count++;
      }
    }
    return count;
  };
  return vowelsCount;

