  var sentences = S.split(/[.?!]/);
  var bored_count = 0;

  for (const sentence of sentences) {
    if (sentence.trim().startsWith('I')) {
      bored_count += 1;
    }
  }

  return bored_count;
}