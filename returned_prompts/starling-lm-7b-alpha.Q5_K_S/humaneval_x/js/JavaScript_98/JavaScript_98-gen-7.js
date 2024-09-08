  let count = 0;
  for (let i = 0; i < s.length; i += 2) {
    if (s[i].match(/[AEIOU]/)) {
      count += 1;
    }
  }
  return count;
}



