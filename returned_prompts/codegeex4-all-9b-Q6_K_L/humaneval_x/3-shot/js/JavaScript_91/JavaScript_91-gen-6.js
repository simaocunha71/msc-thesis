  const boredom = ['i', 'I'];
  const delimiters = ['.', '?', '!'];
  var count = 0;
  var sentences = [];
  var current_sentence = [];

  for (const c of S) {
    if (boredom.includes(c)) {
      current_sentence.push(c);
    } else if (delimiters.includes(c)) {
      current_sentence.push(c);
      sentences.push(current_sentence.join(''));
      current_sentence = [];
    } else {
      current_sentence.push(c);
    }
  }

  for (const sentence of sentences) {
    if (sentence.startsWith('I') || sentence.startsWith('i')) {
      count += 1;
    }
  }

  return count;
}