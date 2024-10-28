  var result = [];
  var current_word = [];
  var current_consonants = 0;

  for (const c of s) {
    if (c == ' ') {
      if (current_consonants == n) {
        result.push(current_word.join(''));
      }
      current_word = [];
      current_consonants = 0;
    } else {
      current_word.push(c);
      if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
        current_consonants += 1;
      }
    }
  }

  if (current_consonants == n) {
    result.push(current_word.join(''));
  }

  return result;
}

