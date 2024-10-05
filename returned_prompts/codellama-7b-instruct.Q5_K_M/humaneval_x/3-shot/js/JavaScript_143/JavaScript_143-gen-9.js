  var result = [];
  var current_word = '';
  for (const c of sentence) {
    if (c == ' ') {
      if (isPrime(current_word.length)) {
        result.push(current_word);
      }
      current_word = '';
    } else {
      current_word += c;
    }
  }
  if (isPrime(current_word.length)) {
    result.push(current_word);
  }
  return result.join(' ');
}



