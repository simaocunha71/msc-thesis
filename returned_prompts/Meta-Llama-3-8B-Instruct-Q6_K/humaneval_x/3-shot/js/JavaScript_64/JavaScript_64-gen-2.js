  let count = 0;
  for (let i = 0; i < s.length; i++) {
    let c = s[i].toLowerCase();
    if (c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u') {
      count++;
    } else if (c === 'y' && i === s.length - 1) {
      count++;
    }
  }
  return count;
}