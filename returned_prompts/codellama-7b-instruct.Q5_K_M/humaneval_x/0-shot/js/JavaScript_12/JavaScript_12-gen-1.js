/* Out of list of strings, return the longest one. Return the first one in case of multiple
  strings of the same length. Return null in case the input list is empty.
  >>> longest([])

  >>> longest(['a', 'b', 'c'])
  'a'
  >>> longest(['a', 'bb', 'ccc'])
  'ccc'
  */
const longest = (strings) => {
  if (strings.length === 0) return null;

  const stringsLengths = strings.map(s => s.length);
  const maxLength = Math.max(...stringsLengths);
  const maxLengthsIndices = stringsLengths.reduce((acc, l, i) => l === maxLength ? [...acc, i] : acc, []);
  return strings[maxLengthsIndices[0]];
}
