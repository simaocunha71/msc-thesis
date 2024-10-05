  let result = [];
  let count = 0;
  let current_word = "";

  for (const c of txt) {
    if (c == ' ') {
      result.push(current_word);
      current_word = "";
    } else if (c == ',') {
      result.push(current_word);
      current_word = "";
    } else if (c >= 'a' && c <= 'z') {
      count += 1;
    } else {
      current_word += c;
    }
  }

  if (current_word.length > 0) {
    result.push(current_word);
  }

  if (result.length == 0) {
    return count;
  }

  return result;
}