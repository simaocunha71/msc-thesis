/*
  removeVowels is a function that takes string and returns string without vowels.
  >>> removeVowels('')
  ''
  >>> removeVowels("abcdef\nghijklm")
  'bcdf\nghjklm'
  >>> removeVowels('abcdef')
  'bcdf'
  >>> removeVowels('aaaaa')
  ''
  >>> removeVowels('aaBAA')
  'B'
  >>> removeVowels('zbcd')
  'zbcd'
  */
const removeVowels = (text) => {
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  return text
    .split('')
    .filter(char => !vowels.includes(char))
    .join('');
};
