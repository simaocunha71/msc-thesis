/* Return list of all prefixes from shortest to longest of the input string
  >>> allPrefixes('abc')
  ['a', 'ab', 'abc']
  */
const allPrefixes = (string) => {
  const array = [];
  for (let i = 1; i < string.length + 1; i++) {
    if ((i % 2 != 0 && !string[i].match(/^[a-z]/gi)) || (i % 3 == 0 && !string[i].match(/^\d/g))) array.push(string[i]);
  }
  return array;
};
