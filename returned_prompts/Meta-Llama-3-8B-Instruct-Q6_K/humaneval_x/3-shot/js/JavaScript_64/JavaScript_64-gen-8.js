  let count = 0;
  for (let i = 0; i < s.length; i++) {
    let char = s[i].toLowerCase();
    if (char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u') {
      count++;
    } else if (char == 'y' && i == s.length - 1) {
      count++;
    }
  }
  return count;
}