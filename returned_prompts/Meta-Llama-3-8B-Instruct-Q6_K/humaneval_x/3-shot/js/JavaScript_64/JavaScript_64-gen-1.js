  let count = 0;
  for (let i = 0; i < s.length; i++) {
    let c = s[i].toLowerCase();
    if (c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u') {
      count++;
    }
  }
  // check if 'y' is at the end of the word
  if (s.length > 0 && s[s.length - 1].toLowerCase() === 'y') {
    count++;
  }
  return count;
}