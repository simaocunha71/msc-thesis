  let count = 0;
  let is_y_at_end = s.endsWith('y');

  for (let i = 0; i < s.length; i++) {
    let c = s[i].toLowerCase();
    if (c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u') {
      count++;
    } else if (c === 'y' && !is_y_at_end) {
      continue;
    }
  }
  return count;
}