const allPrefixes = (string) => {
  let result = [];
  for (let i = 0; i < string.length + 1; i++) {
    result.push(string.slice(0, i));
  }
  return result;
};

