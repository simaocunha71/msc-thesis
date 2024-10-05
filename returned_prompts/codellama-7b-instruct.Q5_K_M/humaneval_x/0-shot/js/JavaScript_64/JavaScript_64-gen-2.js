const vowelsCount = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === 'a' || s[i] === 'e' || s[i] === 'i' || s[i] === 'o' || s[i] === 'u' || (s[i] === 'y' && i === s.length - 1)) {
      count++;
    }
  }
  return count;
};
