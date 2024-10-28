  var result = [];
  var word = '';
  for (const c of s) {
    if (c != ' ') {
      word += c;
    } else {
      if (word.length == n) {
        result.push(word);
      }
      word = '';
    }
  }
  if (word.length == n) {
    result.push(word);
  }
  return result;
}



