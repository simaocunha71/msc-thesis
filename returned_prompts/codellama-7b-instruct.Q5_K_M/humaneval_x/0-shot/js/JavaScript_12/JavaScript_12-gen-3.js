const longest = (strings) => {
  if (!strings.length) {
    return null;
  }
  const [longestString, ...rest] = strings.sort((a, b) => b.length - a.length);
  return longestString;
};


