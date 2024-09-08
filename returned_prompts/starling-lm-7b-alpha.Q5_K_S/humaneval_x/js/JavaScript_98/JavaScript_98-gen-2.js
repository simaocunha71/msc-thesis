  let count = 0;
  for (let i = 0; i < s.length; i += 2) {
    if (s[i] === 'A' || s[i] === 'E' || s[i] === 'I' || s[i] === 'O' || s[i] === 'U') {
      count += 1;
    }
  }
  return count;
}



