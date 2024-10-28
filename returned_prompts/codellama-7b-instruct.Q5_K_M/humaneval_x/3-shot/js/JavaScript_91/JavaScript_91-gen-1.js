  let count = 0;
  let sentences = S.split(/[.?!]/);

  for (sentence of sentences) {
    if (sentence.startsWith("I")) {
      count += 1;
    }
  }
  return count;
}



