  let rev = '';
  let i = 0;
  while (i < string.length) {
    if (rev.indexOf(string.slice(i)) >= 0) {
      return string + rev;
    }
    rev += string[i];
    i++;
  }
  return string + rev;
}