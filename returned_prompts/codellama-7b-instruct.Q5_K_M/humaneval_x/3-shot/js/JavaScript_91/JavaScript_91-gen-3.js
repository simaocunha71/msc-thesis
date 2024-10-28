  var count = 0;
  var sentences = S.split(/[.?!]/);
  for (var sentence of sentences) {
    if (sentence.startsWith("I")) {
      count += 1;
    }
  }
  return count;
}



