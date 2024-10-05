const longest = (strings) => {
  let longestString = null;
  strings.forEach(string => {
    if (longestString === null || string.length > longestString.length) {
      longestString = string;
    }
  });
  return longestString;
};

