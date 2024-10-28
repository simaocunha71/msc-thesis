const countDistinctCharacters = (string) => {
  let result = 0;
  const charSet = {};
  for (let i = 0; i < string.length; i++) {
    const char = string[i].toLowerCase();
    if (!charSet[char]) {
      result++;
      charSet[char] = true;
    }
  }
  return result;
};

