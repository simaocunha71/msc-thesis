  let count = 0;
  let sentence = '';

  for (let i = 0; i < S.length; i++) {
    if (S[i] === '.' || S[i] === '?' || S[i] === '!') {
      if (sentence.trim().toLowerCase().startsWith('i')) {
        count++;
      }
      sentence = '';
    } else {
      sentence += S[i];
    }
  }

  if (sentence.trim().toLowerCase().startsWith('i')) {
    count++;
  }

  return count;
}