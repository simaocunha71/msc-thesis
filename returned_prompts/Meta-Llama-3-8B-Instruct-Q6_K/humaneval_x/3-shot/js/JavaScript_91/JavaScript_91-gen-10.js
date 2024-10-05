  let count = 0;
  let sentences = S.split(/\.|\?|\!/);
  for (const sentence of sentences) {
    if (sentence.trim().startsWith('I')) {
      count++;
    }
  }
  return count;
}