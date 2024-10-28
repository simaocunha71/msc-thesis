const allPrefixes = (string) => {
  const prefixes = [];
  for (let i = 0; i < string.length; i++) {
    prefixes.push(string.slice(0, i + 1));
  }
  return prefixes;
};
