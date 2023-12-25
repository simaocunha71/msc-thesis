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
  return text.replace(/[aeiou]/g, "");
};

describe("removeVowels", () => {
  it(`should return "" when an empty string is passed in`, () => {
    expect(removeVowels('')).toEqual('');
  });

  it(`should return "" when a non-empty string is passed in with no vowels`, () => {
    expect(removeVowels("abcdefghi")).toEqual('bcdfghijklm');
  });

  it(`should return "" when a non-empty string is passed in and only a subset of its letters are vowels`, () => {
    expect(removeVowels("aaBAA")).toEqual("B");
  });
});
