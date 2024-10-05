const countDistinctCharacters = (string) => {
  const charMap = {};
  for (let i = 0; i < string.length; i++) {
    const char = string[i];
    if (!charMap[char]) {
      charMap[char] = 1;
    } else {
      charMap[char]++;
    }
  }
  return Object.keys(charMap).length;
};
