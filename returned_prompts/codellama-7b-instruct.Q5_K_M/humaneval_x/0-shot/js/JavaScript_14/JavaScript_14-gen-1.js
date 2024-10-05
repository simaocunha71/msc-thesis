/* Return list of all prefixes from shortest to longest of the input string
  >>> allPrefixes('abc')
  ['a', 'ab', 'abc']
  */
const allPrefixes = (string) => {
  const prefixes = [];
  for (let i = 0; i < string.length + 1; i++) {
    prefixes.push(string.slice(0, i));
  }
  return prefixes;
};
