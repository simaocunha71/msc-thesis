  let boredomCount = 0;
  let currentSentence = '';
  for (const c of S) {
    if (c === '.' || c === '?' || c === '!') {
      if (currentSentence.startsWith('I')) {
        boredomCount++;
      }
      currentSentence = '';
    } else {
      currentSentence += c;
    }
  }
  if (currentSentence.startsWith('I')) {
    boredomCount++;
  }
  return boredomCount;
}