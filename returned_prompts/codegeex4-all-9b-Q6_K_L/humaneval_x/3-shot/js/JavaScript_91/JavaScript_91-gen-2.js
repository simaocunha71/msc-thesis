  var sentences = S.split(/[.?!]/);
  var count = 0;
  for (const sentence of sentences) {
    sentence = sentence.trim();
    if (sentence.startsWith('I')) {
      count += 1;
    }
  }
  return count;
}



