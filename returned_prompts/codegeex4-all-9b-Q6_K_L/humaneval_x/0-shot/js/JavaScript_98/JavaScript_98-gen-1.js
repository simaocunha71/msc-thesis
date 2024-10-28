const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i += 2) {
    if (i % 2 === 0 && "AEIOU".includes(s[i])) {
      count++;
    }
  }
  return count;
};