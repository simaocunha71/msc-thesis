/* Given a string, find out how many distinct characters (regardless of case) does it consist of
  >>> countDistinctCharacters('xyzXYZ')
  3
  >>> countDistinctCharacters('Jerry')
  4
  */
const countDistinctCharacters = (string) => {
  const letters = string.split("");
  return Math.floor(
    new Set(letters).size() / letters.length | 0
  );
};
