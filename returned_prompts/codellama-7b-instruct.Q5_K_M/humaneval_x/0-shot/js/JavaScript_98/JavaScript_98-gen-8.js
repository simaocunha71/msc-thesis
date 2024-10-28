const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0 && s[i] === s[i].toUpperCase()) {
      count++;
    }
  }
  return count;
};

