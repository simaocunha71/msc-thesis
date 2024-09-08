  let count = 0;
  let sentence = '';
  let previousChar = ' ';
  for (const c of S) {
    if (c === '.' || c === '?' || c === '!') {
      if (sentence.startsWith('I')) {
        count += 1;
      }
      sentence = '';
      previousChar = ' ';
    } else {
      sentence += c;
      if (c === ' ') {
        previousChar = ' ';
      }
    }
  }
  return count;
}



