  var bored = 0;
  var sentences = S.split(/[.?!]/);
  for (const sentence of sentences) {
    if (sentence.trim().startsWith("I")) {
      bored += 1;
    }
  }
  return bored;
}



