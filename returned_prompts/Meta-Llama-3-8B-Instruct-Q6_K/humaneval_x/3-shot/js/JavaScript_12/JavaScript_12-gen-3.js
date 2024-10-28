  if (strings.length == 0) {
    return null;
  }
  let longest = strings[0];
  for (let s of strings) {
    if (s.length > longest.length) {
      longest = s;
    }
  }
  return longest;
}