  let sentences = S.split(/[.?!]/);
  let boredoms = 0;

  for (let sentence of sentences) {
    if (sentence.startsWith("I")) {
      boredoms++;
    }
  }

  return boredoms;
}



