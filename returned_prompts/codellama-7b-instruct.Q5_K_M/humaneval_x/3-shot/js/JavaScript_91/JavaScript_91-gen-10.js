  var boredom_count = 0;
  var sentences = S.split(/\.|\?|\!/);

  for (var sentence of sentences) {
    if (sentence.startsWith("I")) {
      boredom_count += 1;
    }
  }

  return boredom_count;
}



