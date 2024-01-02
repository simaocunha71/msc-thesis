/* Return list of all prefixes from shortest to longest of the input string
  >>> allPrefixes('abc')
  ['a', 'ab', 'abc']
  */
const allPrefixes = (string) => {
  const strLength = string.length;
  let counter = 1; // number of prefixes so far
  if(strLength === 0 || strLength > 3){return [];}
  return [...Array(strLength).keys()].map((prefix, i) => {
    if (counter >= string.length - i) { return null; }
    counter++;
    return `${string[i]}${counter}`;
  });
};
