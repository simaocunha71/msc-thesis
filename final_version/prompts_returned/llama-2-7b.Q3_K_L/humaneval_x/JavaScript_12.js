/* Out of list of strings, return the longest one. Return the first one in case of multiple
  strings of the same length. Return null in case the input list is empty.
  >>> longest([])

  >>> longest(['a', 'b', 'c'])
  'a'
  >>> longest(['a', 'bb', 'ccc'])
  'ccc'
  */
const longest = (strings) => {
  if (!strings || strings.length === 0) return null;

  const maxIndex = strings[0].length;
  const maxLength = strings.reduce((prev, curr, index) => {
    if (index >= maxIndex && prev < curr.length) {
      return prev + curr.length - prev;
    } else if (curr.length > maxLength) {
      return curr.length;
    }
    return prev;
  }, 0);

  // Find index of the longest string and its length
  const [strIndex, strLength] = strings[0].split('').map((c, i) => {
    if (i > maxLength && i === maxLength - 1) return c;
    else return '';
  });

  // Return the first index of the longest string and its length
  return strIndex + strLength;
};
console.log(longest(['hello', 'world']));