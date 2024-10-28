  let count = 0;
  let is_y = false;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === 'a' || s[i] === 'e' || s[i] === 'i' || s[i] === 'o' || s[i] === 'u') {
      count++;
    } else if (s[i] === 'y' && i === s.length - 1) {
      count++;
      is_y = true;
    }
  }
  if (!is_y) {
    return count;
  } else {
    return count - 1;
  }
}
//Note: We subtract 1 when 'y' is at the end of the string because 'y' is counted as a vowel in this case.