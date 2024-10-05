  let boredomCount = 0;
  let sentences = S.split(/[.!?]/);
  for (let sentence of sentences) {
    if (sentence.trim().startsWith('I')) {
      boredomCount++;
    }
  }
  return boredomCount;
}