  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0) {
      if (s[i].toUpperCase() === 'A' || s[i].toUpperCase() === 'E' || s[i].toUpperCase() === 'I' || s[i].toUpperCase() === 'O' || s[i].toUpperCase() === 'U') {
        count++;
      }
    }
  }
  return count;
} 



