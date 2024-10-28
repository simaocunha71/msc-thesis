  var sentences = S.split(/[.?!]/);
  var count = 0;
  for (var i = 0; i < sentences.length; i++) {
    if (sentences[i].trim().startsWith("I")) {
      count += 1;
    }
  }
  return count;
}