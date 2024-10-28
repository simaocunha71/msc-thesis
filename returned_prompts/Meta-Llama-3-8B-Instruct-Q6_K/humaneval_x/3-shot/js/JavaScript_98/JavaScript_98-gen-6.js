  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 == 0 && s[i].toUpperCase() == s[i]) {
      if (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U') {
        count++;
      }
    }
  }
  return count;
}