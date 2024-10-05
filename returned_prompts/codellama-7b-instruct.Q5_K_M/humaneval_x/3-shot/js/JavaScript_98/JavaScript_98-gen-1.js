  let count = 0;

  for (let i = 0; i < s.length; i += 2) {
    if (s[i] == s[i].toUpperCase() && s[i].toUpperCase() == 'A') {
      count++;
    }
  }

  return count;
}



