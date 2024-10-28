  const s = string.split('').reverse().join('');
  let i = 0;
  while (i < s.length && s[i] === string[i]) {
    i++;
  }
  return string + s.slice(i);
}  // End of code.