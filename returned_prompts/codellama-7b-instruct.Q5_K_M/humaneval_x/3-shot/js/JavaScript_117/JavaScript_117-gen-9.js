  var result = [];
  var current_word = '';
  var current_n = 0;

  for (const c of s) {
    if (c == ' ') {
      if (current_n == n) {
        result.push(current_word);
      }
      current_word = '';
      current_n = 0;
    } else {
      if (c.match(/[aeiou]/i) == null) {
        current_n += 1;
      }
      current_word += c;
    }
  }

  if (current_n == n) {
    result.push(current_word);
  }

  return result;
}



