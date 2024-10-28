/* Given a string, find out how many distinct characters (regardless of case) does it consist of
  >>> countDistinctCharacters('xyzXYZ')
  3
  >>> countDistinctCharacters('Jerry')
  4
  */
const countDistinctCharacters = (string) => {
  const lowercaseString = string.toLowerCase();
  const count = {};
  for (let i = 0; i < lowercaseString.length; i++) {
    if (!(lowercaseString[i] in count)) {
      count[lowercaseString[i]] = 0;
    }
    count[lowercaseString[i]]++;
  }
  return Object.keys(count).length;
}
