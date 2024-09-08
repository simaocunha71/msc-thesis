  let result = 0;
  let current_sentence = '';
  for (const c of S) {
    if (c == '.' || c == '?' || c == '!') {
      if (current_sentence.startsWith('I')) {
        result += 1;
      }
      current_sentence = '';
    } else {
      current_sentence += c;
    }
  }
  return result;
}



