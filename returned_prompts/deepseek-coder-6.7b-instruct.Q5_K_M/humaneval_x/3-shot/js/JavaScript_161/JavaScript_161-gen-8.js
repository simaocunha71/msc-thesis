  let new_s = '';
  for (let i = 0; i < s.length; i++) {
    if (s[i].match(/[a-z]/i)) {
      if (s[i] === s[i].toUpperCase()) {
        new_s += s[i].toLowerCase();
      } else {
        new_s += s[i].toUpperCase();
      }
    } else {
      new_s += s[i];
    }
  }
  return new_s;
}



