  var count = 0;
  var sentence_end = ['.', '?', '!'];
  var sentence = '';

  for (const c of S) {
    if (c == '.' || c == '?' || c == '!') {
      if (sentence.startsWith('I')) {
        count += 1;
      }
      sentence = '';
    } else {
      sentence += c;
    }
  }

  return count;
}



